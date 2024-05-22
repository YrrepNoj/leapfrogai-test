"""CRUD Operations for FileObject"""

from pydantic import Field

from openai.types import FileObject
from supabase_py_async import AsyncClient

from leapfrogai_api.data.async_mixin import AsyncMixin
from leapfrogai_api.data.crud_base import CRUDBase
from leapfrogai_api.routers.supabase_session import get_user_session


class AuthFileObject(FileObject):
    """A wrapper for the FileObject that includes a user_id for auth"""

    user_id: str = Field(default="")


class CRUDFileObject(AsyncMixin, CRUDBase[AuthFileObject]):
    """CRUD Operations for FileObject"""

    async def __ainit__(self, jwt: str, table_name: str = "file_objects"):
        db: AsyncClient = await get_user_session(jwt)
        CRUDBase.__init__(
            self, jwt=jwt, db=db, model=AuthFileObject, table_name=table_name
        )

    async def create(self, object_: FileObject) -> AuthFileObject | None:
        """Create a new file object."""
        user_id: str = (await self.db.auth.get_user(self.jwt)).user.id
        return await super().create(
            object_=AuthFileObject(user_id=user_id, **object_.model_dump())
        )

    async def get(self, id_: str) -> AuthFileObject | None:
        """Get a file object by its ID."""
        return await super().get(id_=id_)

    async def list(self) -> list[AuthFileObject] | None:
        """List all file objects."""
        return await super().list()

    async def update(self, id_: str, object_: FileObject) -> AuthFileObject | None:
        """Update a file object by its ID."""
        user_id: str = (await self.db.auth.get_user(self.jwt)).user.id
        return await super().update(
            id_=id_, object_=AuthFileObject(user_id=user_id, **object_.model_dump())
        )

    async def delete(self, id_: str) -> bool:
        """Delete a file object by its ID."""
        return await super().delete(id_=id_)
