"""CRUD Operations for VectorStore."""

import time

from pydantic import Field
from openai.types.beta import VectorStore
from supabase_py_async import AsyncClient
from leapfrogai_api.data.crud_base import CRUDBase


class AuthVectorStore(VectorStore):
    """A wrapper for the VectorStore that includes a user_id for auth"""

    user_id: str = Field(default="")


class CRUDVectorStore(CRUDBase[AuthVectorStore]):
    """CRUD Operations for VectorStore"""

    def __init__(self, db: AsyncClient):
        super().__init__(db=db, model=AuthVectorStore, table_name="vector_store")

    async def create(self, object_: VectorStore) -> AuthVectorStore | None:
        """Create new vector store."""
        user_id: str = (await self.db.auth.get_user()).user.id
        return await super().create(
            object_=AuthVectorStore(user_id=user_id, **object_.model_dump())
        )

    async def get(self, id_: str) -> AuthVectorStore | None:
        """Get a vector store by its ID."""

        vector_store: AuthVectorStore | None = await super().get(id_=id_)

        if await self.delete_when_expired(vector_store):
            return None

        return vector_store

    async def list(self) -> list[AuthVectorStore] | None:
        """List all vector stores."""

        vector_stores: list[AuthVectorStore] | None = await super().list()
        non_expired_vector_stores: list[AuthVectorStore] | None = None

        if vector_stores:
            # Iterate through each vector store and delete expired entries
            for vector_store in vector_stores:
                vector_store_deleted: bool = await self.delete_when_expired(
                    vector_store
                )

                if vector_store_deleted:
                    continue
                else:
                    if non_expired_vector_stores:
                        non_expired_vector_stores.append(vector_store)
                    else:
                        non_expired_vector_stores = [vector_store]

        return non_expired_vector_stores

    async def update(self, id_: str, object_: VectorStore) -> AuthVectorStore | None:
        """Update a vector store by its ID."""

        dict_ = object_.model_dump()
        del dict_["bytes"]  # Automatically calculated by DB

        data, _count = (
            await self.db.table(self.table_name).update(dict_).eq("id", id_).execute()
        )

        _, response = data

        if response:
            return self.model(**response[0])
        return None

    async def delete(self, id_: str) -> bool:
        """Delete a vector store by its ID."""
        return await super().delete(id_=id_)

    async def delete_when_expired(self, vector_store: AuthVectorStore | None) -> bool:
        """Delete vector stores when they are expired"""

        if vector_store and vector_store.expires_at and vector_store.expires_after:
            current_time = int(time.time())

            if current_time > vector_store.expires_at:
                await self.delete(id_=vector_store.id)
                return True
        return False
