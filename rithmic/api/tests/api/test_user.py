import email
from django.http import response
import pytest

pytestmark = pytest.mark.django_db


def test_register_user(client):
    payload = {
        "first_name": "Biko",
        "last_name": "Codes",
        "email":  "b@c.com",
        "password":  "test"
    }
    response = client.post("/api/register/", payload)

    data = response.data

    assert data["first_name"] == payload["first_name"]
    assert data["last_name"] == payload["last_name"]
    assert data["email"] == payload["email"]
    assert "password" not in data
    


def test_login_user(user, client):
    
    response = client.post("/api/login/", dict(email="b@c.com", password="test"))

    assert response.status_code == 200


def test_login_unregistered_user(client):
    response = client.post("/api/login/", dict(email="t@t.com", password="tacos"))

    assert response.status_code == 403


def test_get_me(user, authenticated_user):
    
    response = authenticated_user.get("/api/me/")

    assert response.status_code == 200

    data = response.data

    assert data["id"] == user.id
    assert data["email"] == user.email


def test_logout(authenticated_user):
    response = authenticated_user.post("/api/logout/")

    assert response.status_code == 200 
    assert response.data["message"] == "so long farewell"







