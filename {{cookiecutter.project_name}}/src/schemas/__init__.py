"""
O esquemas devem extender a class BaseModel do pacote pydantic

e.g:
    from pydantic import BaseModel

    class User(BaseModel):
        id: int
        name: str

"""
from typing import Optional, List
from pydantic import BaseModel


class UserPayload(BaseModel):
    name: str
    email: Optional[str]


class UserResponse(BaseModel):
    id: int
    name: str
    email: Optional[str]


class UserList(BaseModel):
    users: List[UserResponse]


class SimpleMessage(BaseModel):
    message: str
