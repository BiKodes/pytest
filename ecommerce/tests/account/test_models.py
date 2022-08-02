import email

import pytest
from conftest import customer


def test_customer_str(customer):
    assert customer.__str__() == "BikoCodes"


def test_customer_str(adminuser):
    assert adminuser.__str__() == "admin_user"


def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="")
    assert str(e.value) == "Customer Account: You must provide an email address"


def test_customer_email_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="j.com")
    assert str(e.value) == "You must provide a valid email address"


def test_adminuser_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_staff=True, is_superuser=True)
    assert str(e.value) == "Superuser Account: You must provide an email address"


def test_adminuser_email_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="j.com", is_staff=True, is_superuser=True)
    assert str(e.value) == "You must provide a valid email address"


def test_adminuser_email_not_staff(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_staff=False, is_superuser=True)
    assert str(e.value) == "Superuser must be assigned to is_staff=True."


def test_adminuser_email_not_superuser(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="j.com", is_staff=True, is_superuser=False)
    assert str(e.value) == "Superuser must be assigned to is_superuser=True."


def test_address_str(address):
    name = address.full_name
    assert address.__str__() == name + " Address"
