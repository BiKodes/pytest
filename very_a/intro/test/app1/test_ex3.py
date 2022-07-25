import pytest

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True

def test_set_check_username1(user_1):
    print("check-user1")
    assert user_1.username == "test-user"

def test_set_check_username2(user_2):
    print("check-user2")
    assert user_2.username == "Test-User"



