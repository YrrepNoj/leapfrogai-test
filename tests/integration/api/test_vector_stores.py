"""Test the API endpoints for assistants."""
import json
import os

import pytest
from fastapi import Response, status
from fastapi.testclient import TestClient
from openai.types.beta import VectorStore, VectorStoreDeleted
from openai.types.beta.vector_store import ExpiresAfter
from langchain_core.embeddings.fake import FakeEmbeddings

import leapfrogai_api.backend.rag.index
from leapfrogai_api.backend.types import (
    CreateVectorStoreRequest,
    ModifyVectorStoreRequest,
)
from leapfrogai_api.routers.openai.vector_stores import router as vector_store_router
from leapfrogai_api.routers.openai.files import router as files_router

INSTRUCTOR_XL_EMBEDDING_SIZE: int = 768


class FakeEmbeddingsWrapper(FakeEmbeddings):

    def __init__(self):
        super().__init__(size=INSTRUCTOR_XL_EMBEDDING_SIZE)


class MissingEnvironmentVariable(Exception):
    pass


headers: dict[str, str] = {}

try:
    headers = {"Authorization": f"Bearer {os.environ['SUPABASE_USER_JWT']}"}
except KeyError as exc:
    raise MissingEnvironmentVariable(
        "SUPABASE_USER_JWT must be defined for the test to pass. "
        "Please check the api README for instructions on obtaining this token."
    ) from exc

vector_store_client = TestClient(vector_store_router, headers=headers)
files_client = TestClient(files_router, headers=headers)


# Read in file for use with vector store files
@pytest.fixture(scope="session", autouse=True)
def read_testfile():
    """Read the test file content."""

    with open(
            os.path.dirname(__file__) + "/../../../tests/data/test.txt", "rb"
    ) as testfile:
        testfile_content = testfile.read()

    return testfile_content


# Adds file to Supabase
@pytest.fixture(scope="session", autouse=True)
def create_file(read_testfile):  # pylint: disable=redefined-outer-name, unused-argument
    """Create a file for testing. Requires a running Supabase instance."""

    file_response = files_client.post(
        "/openai/v1/files",
        files={"file": ("test.txt", read_testfile, "text/plain")},
        data={"purpose": "assistants"},
    )

    json_data = json.loads(file_response.text)

    return json_data


vector_store_response: Response


# Create a vector store with the previously created file and fake embeddings
@pytest.fixture(scope="session", autouse=True)
def create_vector_store(create_file):
    """Create a vector store for testing. Requires a running Supabase instance."""

    global vector_store_response  # pylint: disable=global-statement

    # Mock out the embeddings creation using a fake
    leapfrogai_api.backend.rag.index.embeddings_type = FakeEmbeddingsWrapper

    request = CreateVectorStoreRequest(
        file_ids=[create_file['id']],
        name="test",
        expires_after=ExpiresAfter(anchor="last_active_at", days=0),
        metadata={},
    )

    vector_store_response = vector_store_client.post(
        "/openai/v1/vector_stores", json=request.model_dump()
    )


def test_create():
    """Test creating a vector store. Requires a running Supabase instance."""
    assert vector_store_response.status_code == status.HTTP_200_OK
    assert VectorStore.model_validate(
        vector_store_response.json()
    ), "Create should create a VectorStore."


def test_get():
    """Test getting a vector store. Requires a running Supabase instance."""
    vector_store_id = vector_store_response.json()["id"]
    get_response = vector_store_client.get(f"/openai/v1/vector_stores/{vector_store_id}")
    assert get_response.status_code == status.HTTP_200_OK
    assert VectorStore.model_validate(
        get_response.json()
    ), f"Get should return VectorStore {vector_store_id}."


def test_list():
    """Test listing vector stores. Requires a running Supabase instance."""
    list_response = vector_store_client.get("/openai/v1/vector_stores")
    assert list_response.status_code == status.HTTP_200_OK
    for vector_store_object in list_response.json()["data"]:
        assert VectorStore.model_validate(
            vector_store_object
        ), "Should return a list of VectorStore."


def test_modify():
    """Test modifying a vector store. Requires a running Supabase instance."""
    vector_store_id = vector_store_response.json()["id"]
    request = ModifyVectorStoreRequest(
        file_ids=[],
        name="test1",
        expires_after=ExpiresAfter(anchor="last_active_at", days=0),
        metadata={},
    )

    modify_response = vector_store_client.post(
        f"/openai/v1/vector_stores/{vector_store_id}",
        json=request.model_dump(),
    )
    assert modify_response.status_code == status.HTTP_200_OK
    assert VectorStore.model_validate(
        modify_response.json()
    ), "Should return a VectorStore."
    assert modify_response.json()["name"] == "test1", "Should be modified."


def test_get_modified():
    """Test getting a modified vector store. Requires a running Supabase instance."""
    vector_store_id = vector_store_response.json()["id"]
    get_modified_response = vector_store_client.get(f"/openai/v1/vector_stores/{vector_store_id}")
    assert get_modified_response.status_code == status.HTTP_200_OK
    assert VectorStore.model_validate(
        get_modified_response.json()
    ), f"Get should return modified VectorStore {vector_store_id}."
    assert get_modified_response.json()["name"] == "test1", "Should be modified."


def test_delete():
    """Test deleting a vector store. Requires a running Supabase instance."""
    vector_store_id = vector_store_response.json()["id"]
    delete_response = vector_store_client.delete(f"/openai/v1/vector_stores/{vector_store_id}")
    assert delete_response.status_code == status.HTTP_200_OK
    assert VectorStoreDeleted.model_validate(
        delete_response.json()
    ), "Should return a VectorStoreDeleted object."
    assert delete_response.json()["deleted"] is True, "Should be able to delete."


def test_delete_twice():
    """Test deleting a vector store twice. Requires a running Supabase instance."""
    vector_store_id = vector_store_response.json()["id"]
    delete_response = vector_store_client.delete(f"/openai/v1/vector_stores/{vector_store_id}")
    assert delete_response.status_code == status.HTTP_200_OK
    assert VectorStoreDeleted.model_validate(
        delete_response.json()
    ), "Should return a VectorStoreDeleted object."
    assert (
            delete_response.json()["deleted"] is False
    ), "Should not be able to delete twice."


def test_get_nonexistent():
    """Test getting a nonexistent vector store. Requires a running Supabase instance."""
    vector_store_id = vector_store_response.json()["id"]
    get_response = vector_store_client.get(f"/openai/v1/vector_stores/{vector_store_id}")
    assert get_response.status_code == status.HTTP_200_OK
    assert (
            get_response.json() is None
    ), f"Get should not return deleted VectorStore {vector_store_id}."
