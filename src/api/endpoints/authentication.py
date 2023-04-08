from datetime import timedelta
from typing import Annotated

from pydantic import BaseModel
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from api.dependencies import get_settings, get_db
from api.dependencies.authentication import authenticate_user, create_access_token
from api.exceptions import UnauthorisedException

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    settings=Depends(get_settings),
    db=Depends(get_db),
):
    user = authenticate_user(form_data.username, form_data.password, db=db)
    if not user:
        raise UnauthorisedException
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
        settings=settings,
    )
    return {"access_token": access_token, "token_type": "bearer"}
