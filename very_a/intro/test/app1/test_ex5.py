from distutils.command.build import build
from itertools import count
import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_new_user(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    print(count)
    print(user_factory.username)
    assert True

def test_new_user1(new_user4):
    print(new_user4.username)
    assert True