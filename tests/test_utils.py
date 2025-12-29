from typing import Generator

import pytest

from src.models import Category
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

    products_str = category1.products
    assert isinstance(products_str, str)

    assert "Samsung Galaxy C23 Ultra" in products_str
    assert "180000 руб." in products_str
    assert "Остаток: 5 шт." in products_str

    assert len(products_str.split("\n")) == 3

    category2 = categories[1]
    assert isinstance(category2, Category)
    assert category2.name == "Телевизоры"

    products_str_2 = category2.products
    assert '55" QLED 4K' in products_str_2
    assert "123000 руб." in products_str_2

    assert len(products_str_2.split("\n")) == 1

    assert Category.category_count == 2
    assert Category.product_count == 4
