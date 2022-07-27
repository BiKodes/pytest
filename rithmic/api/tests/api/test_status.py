from django.http import response
import pytest

from status import models

@pytest.mark.django_db 
def test_create_status(authenticated_user, user):
    payload = dict(
        content = "This is a good test. My heart beats for tests"
    )

    response = authenticated_user.post("/api/status/", payload)

    data = response.data

    status_from_db = models.Status.objects.all().first()

    assert data["content"] == status_from_db.content
    assert data["id"] == status_from_db.id
    assert data["user"]["id"] == user.id

@pytest.mark.django_db
def test_get_user_status(authenticated_user, user):
    models.Status.objects.create(user_id=user.id, content="Another test status")
    models.Status.objects.create(user_id=user.id, content="I am a Pythonista")

    response = authenticated_user.get("/api/status")

    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_get_user_status_detail(authenticated_user, user):
    status = models.Status.objects.create(user_id=user.id, content="Another test status")
    
    response = authenticated_user.get(f"/api/status/{status.id}/")

    assert response.status_code == 200

    data = response.data

    assert data["id"] == status.id
    assert data["content"] == status.content

@pytest.mark.django_db
def test_get_user_status_detail_404(authenticated_user):
    response = authenticated_user.get("/api/status/0/")

    assert response.status_code == 404

@pytest.mark.django_db
def test_put_user_status(authenticated_user, user):
    status = models.Status.objects.create(user_id=user.id, content="Another test status")

    payload = dict(content="I just updated my status")
    response = authenticated_user.put(f"/api/status/{status.id}/", payload)

    status.refresh_from_db()
    data = response.data

    assert data["id"] == status.id
    assert status.content == payload["content"]

@pytest.mark.django_db
def test_delete_user_status(authenticated_user, user):
    status = models.Status.objects.create(user_id=user.id, content="Another test status")
    response = authenticated_user.delete(f"/api/status/{status.id}/")

    assert response.status_code == 204

    with pytest.raises(models.Status.DoesNotExist):
        status.refresh_from_db()
