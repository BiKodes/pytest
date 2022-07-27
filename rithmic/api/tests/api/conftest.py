import pytest

from user import services as user_services

from rest_framework.test import APIClient

@pytest.fixture
def user():
    user_dc = user_services.UserDataClass(
        first_name="Biko",
        last_name="Codes",
        email="b@c.com",
        password="test"
    )

    user = user_services.create_user(user_dc=user_dc)

    return user

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def authenticated_user(user, client):
    client.post("/api/login/", dict(email=user.email, password="test"))
    return client