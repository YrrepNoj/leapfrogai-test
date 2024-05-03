"""Test the API endpoints for assistants."""

from fastapi.testclient import TestClient
from openai.types.beta import Assistant, AssistantDeleted

from leapfrogai_api.routers.openai.assistants import router
from leapfrogai_api.backend.types import (
    CreateAssistantRequest,
    ModifyAssistantRequest,
)

client = TestClient(router)


def test_assistants():
    """Test creating an assistant. Requires a running Supabase instance."""
    request = CreateAssistantRequest(
        model="test",
        name="test",
        description="test",
        instructions="test",
        tools=[{"type": "file_search"}],
        tool_resources={},
        metadata={},
        temperature=1.0,
        top_p=1.0,
        response_format="auto",
    )

    create_response = client.post("/openai/v1/assistants", json=request.model_dump())
    assert create_response.status_code == 200
    assert Assistant.model_validate(create_response.json())

    list_response = client.get("/openai/v1/assistants")
    assert list_response.status_code == 200
    for assistant_object in list_response.json():
        assert Assistant.model_validate(
            assistant_object
        ), "Should return a list of Assistants."

    get_response = client.get(f"/openai/v1/assistants/{create_response.json()['id']}")
    assert get_response.status_code == 200
    assert Assistant.model_validate(get_response.json()), "Should return an Assistant."

    request = ModifyAssistantRequest(
        model="test1",
        name="test1",
        description="test1",
        instructions="test1",
        tools=[{"type": "file_search"}],
        tool_resources={},
        metadata={},
        temperature=1.0,
        top_p=1.0,
        response_format="auto",
    )

    modify_response = client.post(
        f"/openai/v1/assistants/{create_response.json()['id']}",
        json=request.model_dump(),
    )
    assert modify_response.status_code == 200
    assert Assistant.model_validate(
        modify_response.json()
    ), "Should return a Assistant."
    assert modify_response.json()["model"] == "test1", "Should be modified."

    get_modified_response = client.get(
        f"/openai/v1/assistants/{create_response.json()['id']}"
    )
    assert get_modified_response.status_code == 200
    assert Assistant.model_validate(
        get_modified_response.json()
    ), "Should return a Assistant."
    assert get_modified_response.json()["model"] == "test1", "Should be modified."

    delete_response = client.delete(
        f"/openai/v1/assistants/{create_response.json()['id']}"
    )
    assert delete_response.status_code == 200
    assert AssistantDeleted.model_validate(
        delete_response.json()
    ), "Should return a AssistantDeleted object."
    assert delete_response.json()["deleted"] is True, "Should be able to delete."

    delete_response = client.delete(
        f"/openai/v1/assistants/{create_response.json()['id']}"
    )
    assert (
        delete_response.status_code == 200
    ), "Should return 200 even if the assistant is not found."
    assert AssistantDeleted.model_validate(
        delete_response.json()
    ), "Should return a AssistantDeleted object."
    assert (
        delete_response.json()["deleted"] is False
    ), "Should not be able to delete twice."

    # Make sure the assistant is not still present
    get_response = client.get(f"/openai/v1/assistants/{create_response.json()['id']}")
    assert get_response.status_code == 200
    assert get_response.json() is None
