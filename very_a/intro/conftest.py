import pytest

from pytest_factoryboy import register
from test.app1.factories import UserFactory, CategoryFactory, ProductFactory
from django.contrib.auth.models import User

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)

@pytest.fixture
def new_user4(db, user_factory):
    user = user_factory.create()
    return user

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.fixture()
def user_2(db):
    user = User.objects.create_user("Test-User")
    print("create-user")  
    return user

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "t@t.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True
    ):

        user = User.objects.create_user(
            username = username,
            password = password,
            first_name = first_name,   
            last_name = last_name,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active
        )

        return user
    return create_app_user

@pytest.fixture
def new_user1(db, new_user_factory):
    return new_user_factory("Test_User", "password", "MyName")

@pytest.fixture
def new_user2(db, new_user_factory):
    return new_user_factory("Test_User", "password", "MyName", is_staff="True")