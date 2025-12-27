from typing import Generator

import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> Generator[None, None, None]:
    Category.category_count = 0
    Category.product_count = 0
    yield


def test_product_initialization() -> None:
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_category_initialization_with_products() -> None:
    product1 = Product("Samsung", "Описание", 100000.0, 5)
    product2 = Product("Xiaomi", "Описание", 30000.0, 10)

    category = Category(name="Смартфоны", description="Категория смартфонов", products=[product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert isinstance(category.products, list)
    assert len(category.products) == 2
    assert category.products[0] is product1
    assert category.products[1] is product2


def test_category_class_counters_single_category() -> None:
    product = Product("TV", "Описание", 120000.0, 3)

    Category(name="Телевизоры", description="Категория ТВ", products=[product])

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_class_counters_multiple_categories() -> None:
    product1 = Product("Samsung", "Описание", 100000.0, 5)
    product2 = Product("Iphone", "Описание", 200000.0, 7)
    product3 = Product("TV", "Описание", 150000.0, 2)

    Category(name="Смартфоны", description="Категория смартфонов", products=[product1, product2])

    Category(name="Телевизоры", description="Категория ТВ", products=[product3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_without_products() -> None:
    category = Category(name="Пустая категория", description="Без товаров", products=[])

    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0
