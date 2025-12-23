from typing import Generator

import pytest

from src.models import Category, Product
from src.utils import load_categories_from_json


@pytest.fixture(autouse=True)
def reset_category_counters() -> Generator[None, None, None]:
    Category.category_count = 0
    Category.product_count = 0
    yield


def test_load_categories_from_json() -> None:
    categories = load_categories_from_json("data/products.json")

    assert isinstance(categories, list)
    assert len(categories) == 2

    category1 = categories[0]
    assert isinstance(category1, Category)
    assert category1.name == "Смартфоны"
    assert len(category1.products) == 3

    product1 = category1.products[0]
    assert isinstance(product1, Product)
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    category2 = categories[1]
    assert isinstance(category2, Category)
    assert category2.name == "Телевизоры"
    assert len(category2.products) == 1

    product2 = category2.products[0]
    assert isinstance(product2, Product)
    assert product2.name == '55" QLED 4K'
    assert product2.price == 123000.0

    assert Category.category_count == 2
    assert Category.product_count == 4
