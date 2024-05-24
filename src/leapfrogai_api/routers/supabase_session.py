"""Supabase session dependency."""

import os
from typing import Annotated
from fastapi import Depends, status, HTTPException, Header
from supabase_py_async import AsyncClient, create_client, ClientOptions
from httpx import HTTPStatusError
from gotrue import errors, types
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()


async def init_supabase_client(
    auth_creds: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    refresh_token: str = Header(default="dummy"), 
) -> AsyncClient:
    """
    Returns an authenticated Supabase client using the provided user's JWT token

    Parameters:
        auth_creds (HTTPAuthorizationCredentials): the auth credentials for the user that include the bearer token
        refresh_token (str): the refresh token to use when the JWT token expires

    Returns:
        user_client (AsyncClient): a client instantiated with a session associated with the JWT token
    """

    client: AsyncClient = await create_client(
        supabase_key=os.getenv("SUPABASE_ANON_KEY"),
        supabase_url=os.getenv("SUPABASE_URL"),
        access_token=auth_creds.credentials,
        options=ClientOptions(auto_refresh_token=refresh_token != "dummy"),
    )

    # Set up a session for this client, a dummy refresh_token is used to prevent validation errors
    await client.auth.set_session(
        access_token=auth_creds.credentials, refresh_token=refresh_token
    )

    await validate_user_authorization(
        session=client, authorization=auth_creds.credentials
    )

    return client


Session = Annotated[AsyncClient, Depends(init_supabase_client)]


async def validate_user_authorization(session: Session, authorization: str):
    """
    Check if the provided user's JWT token is valid, raises a 403 if not

    Parameters:
        session (Session): the default anonymous session
        authorization (str): the JWT token for the user
    """

    authorized = True

    if authorization:
        api_key: str = authorization.replace("Bearer ", "")

        try:
            user_response: types.UserResponse = await session.auth.get_user(api_key)

            if user_response is None:
                authorized = False
        except HTTPStatusError:
            authorized = False
        except errors.AuthApiError:
            authorized = False
    else:
        authorized = False

    if not authorized:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
