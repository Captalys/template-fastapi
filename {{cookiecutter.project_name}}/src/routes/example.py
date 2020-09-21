from fastapi import APIRouter
from fastapi.responses import JSONResponse


from src.schemas import UserResponse, SimpleMessage, UserList, UserPayload
from src.models.fake_db import get_user, get_users, save_user, remove_user, update_user

router = APIRouter()


@router.get("/users/", tags=['users'], description="List all users", status_code=200, response_model=UserList)
def get_all_users():
    return dict(users=get_users())


@router.get("/users/{user_id}", tags=['users'], responses={
    200: dict(model=UserResponse, description="User found"),
    404: dict(model=SimpleMessage, description="User not found")
})
def get_user_by_id(user_id: int):
    user = get_user(user_id)
    if not user:
        return JSONResponse(status_code=404, content=dict(message="User not found"))
    return user


@router.post("/users/", tags=['users'], status_code=201, responses={
    201: dict(model=UserResponse, description="User created"),
    400: dict(model=SimpleMessage, description="Invalid payload")
})
def create_user(user: UserPayload):
    status, data = save_user(user)
    if not status:
        return JSONResponse(status_code=400, content=dict(message=data))
    return data


@router.delete("/users/{user_id}", tags=['users'],  status_code=200, response_model=SimpleMessage,
               description="User deleted.")
def delete_user(user_id: int):
    remove_user(user_id)
    return JSONResponse(status_code=200, content=dict(message="User removed"))


@router.patch("/users/{user_id}", tags=['users'], responses={
    200: dict(model=UserResponse, description="User updated."),
    404: dict(model=SimpleMessage, description="User not found")
})
def patch_user(user_id: int, user_data: UserPayload):
    status, data = update_user(user_id, user_data)
    if not status:
        return JSONResponse(status_code=400, content=dict(message=data))
    return JSONResponse(status_code=200, content=data)
