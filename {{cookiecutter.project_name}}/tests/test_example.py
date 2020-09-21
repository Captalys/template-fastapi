def test_list_users(client):
    users = client.get("/users/")
    assert len(users.json().get('users')) == 0


def test_create_a_user(client, user):
    result = client.post("/users/", json=user)
    print(f"result: {result.json()}")
    assert result.status_code == 201
    user.update(dict(id=result.json().get("id")))
    assert result.json() == user


def test_get_user_by_id(client):
    result = client.get(f"/users/23")
    assert result.status_code == 200
