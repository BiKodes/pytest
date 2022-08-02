import pytest
from django.http import response
from ecommerce.apps.account.forms import RegistrationForm, UserAddressForm


@pytest.mark.parametrize(
    "full_name, phone, address_line, address_line2, town_city, postcode, validity",
    [
        ("biko", "00000", "add1", "add2", "town", "254", True), 
        ("", "00000", "add1", "add2", "town", "254", False)
    ],
)
def test_customer_add(full_name, phone, address_line, address_line2, town_city, postcode, validity):
    form = UserAddressForm(
        data={
            "full_name": full_name,
            "phone": phone,
            "address_line": address_line,
            "address_line2": address_line2,
            "town_city": town_city,
            "postcode": postcode,
        }
    )
    assert form.is_valid() is validity


def test_customer_create_address(client, customer):
    user = customer
    client.force_login(user)
    response = client.post(
        "/account/add_address/",
        data={
            "full_name": "test",
            "phone": "254",
            "address_line": "test",
            "address_line2": "test",
            "town_city": "test",
            "postcode": "254",
        },
    )
    assert response.status_code == 302


@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", "t@t.com", "1234j", "1234j", True),
        ("user1", "t@t.com", "1234j", "", False),
        ("user1", "t@t.com", "1234j", "1234b", False),
        ("user1", "t@.com", "1234j", "1234j", False),
    ],
)
@pytest.mark.django_db
def test_create_account(user_name, email, password, password2, validity):
    form = RegistrationForm(
        data={
            "user_name": user_name, 
            "email": email, 
            "password": password, 
            "password2": password2},
    )
    assert form.is_valid() is validity


@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", "t@t.com", "1234j", "1234j", 200),
        ("user1", "t@t.com", "1234j", "1234", 400),
        ("user1", "", "1234j", "1234", 400)
    ],
)
@pytest.mark.django_db
def test_create_account_view(client, user_name, email, password, password2, validity):
    response = client.post(
        "/account/register/",
        data={
            "user_name": user_name, 
            "email": email, 
            "password": password, 
            "password2": password2
        },
    )
    assert response.status_code == validity

def test_account_register_redirect(client, customer):
    user = customer
    client.force_login(user)
    response = client.get("/account/register/")
    assert response.status_code == 302

@pytest.mark.django_db
def test_account_register_render(client):
    response = client.get("/account/register/") 