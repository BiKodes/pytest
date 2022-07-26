from itertools import product
import pytest

from app1.models import Product

def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True

@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", "Slug", "4.99", "3.99", True),
        ("NewTitle", 1, "NewDescription", "Slug", "", "3.99", False),
    ]
)
@pytest.mark.django_db
def test_product_instance(
    product_factory, title, category, description, slug, regular_price, discount_price, validity
):
    test = product_factory(
        title = title,
        category_id = category,
        description = description,
        slug = slug,
        regular_price = regular_price,
        discount_price = discount_price
    )

    item = Product.objects.all().count()
    print(item)
    assert item == validity


