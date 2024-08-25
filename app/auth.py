from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str

def fake_decode_token(token: str):
    return User(username="fakeuser")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = fake_decode_token(token)
        return user
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials"
        )
