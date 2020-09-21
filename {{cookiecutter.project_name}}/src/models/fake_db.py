from typing import Tuple, Union, Dict

from src.schemas import UserPayload


FAKE_DB = list()


def get_user(user_id: int):
    for user in FAKE_DB:
        if user.get('id') == user_id:
            return user
    return None


def get_users():
    return FAKE_DB


def save_user(user_data: UserPayload) -> Tuple[bool, Union[str, Dict]]:
    user_id = 1
    for user in FAKE_DB:
        print(f"User {user}")
        if user.get('name') == user_data.name:
            return False, "User already exists."
        user_id = user.get('id') + 1
    user = user_data.dict()
    user.update(dict(id=user_id))
    FAKE_DB.append(user)
    return True, user


def remove_user(user_id):
    for user in FAKE_DB:
        if user.get('id') == user_id:
            FAKE_DB.remove(user)
    return


def update_user(user_id: int, user_data: UserPayload) -> Tuple[bool, Union[str, Dict]]:
    for user in FAKE_DB:
        if user.get('id') == user_id:
            user.update(user_data.dict())
            return True, user
    return False, "User not found"
