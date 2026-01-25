import json
from typing import Generator

import pytest

from src.models import Category
from src.utils import load_categories_from_json


@pytest.fixture(autouse=True)
def reset_category_counters() -> Generator[None, None, None]:
    Category.category_count = 0
    Category.product_count = 0
    yield


def test_load_categories_from_json(tmp_path) -> None:
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]

    json_file = tmp_path / "products.json"
    json_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    categories = load_categories_from_json(str(json_file))

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
