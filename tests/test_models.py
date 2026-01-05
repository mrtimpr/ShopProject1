from typing import Any, Dict, Generator, List

import pytest

from src.models import Category, CategoryIterator, Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> Generator[None, None, None]:
    Category.category_count = 0
    Category.product_count = 0
    yield


# Product


def test_product_initialization() -> None:
    product = Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_str() -> None:
    product = Product("Samsung", "Описание", 100000.0, 5)

    assert str(product) == "Samsung, 100000 руб. Остаток: 5 шт."


def test_product_add() -> None:
    product1 = Product("A", "Описание", 100.0, 10)
    product2 = Product("B", "Описание", 200.0, 2)

    assert product1 + product2 == 1400


def test_product_add_invalid_type() -> None:
    product = Product("A", "Описание", 100.0, 1)

    with pytest.raises(TypeError):
        _ = product + 10  # type: ignore


def test_product_price_setter_invalid_price(
    capsys: pytest.CaptureFixture[str],
) -> None:
    product = Product("Test", "Test", 1000.0, 1)

    product.price = -100
    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000.0


def test_product_price_decrease_declined(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Test", "Test", 1000.0, 1)

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 500

    assert product.price == 1000.0


def test_product_price_decrease_confirmed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    product = Product("Test", "Test", 1000.0, 1)

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 500

    assert product.price == 500


def test_new_product_creates_new() -> None:
    data: Dict[str, Any] = {
        "name": "Samsung",
        "description": "Описание",
        "price": 100000.0,
        "quantity": 5,
    }

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Samsung"
    assert product.quantity == 5
    assert product.price == 100000.0


def test_new_product_merges_duplicate(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "y")

    existing = Product("Samsung", "Описание", 90000.0, 5)
    products: List[Product] = [existing]

    data: Dict[str, Any] = {
        "name": "Samsung",
        "description": "Описание",
        "price": 100000.0,
        "quantity": 3,
    }

    result = Product.new_product(data, products)

    assert result is existing
    assert existing.quantity == 8
    assert existing.price == 100000.0


# Category


def test_category_initialization_with_products() -> None:
    product1 = Product("Samsung", "Описание", 100000.0, 5)
    product2 = Product("Xiaomi", "Описание", 30000.0, 10)

    category = Category(
        name="Смартфоны",
        description="Категория смартфонов",
        products=[product1, product2],
    )

    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"

    products_str = category.products
    assert "Samsung, 100000 руб. Остаток: 5 шт." in products_str
    assert "Xiaomi, 30000 руб. Остаток: 10 шт." in products_str


def test_category_str() -> None:
    product1 = Product("Samsung", "Описание", 100000.0, 5)
    product2 = Product("Xiaomi", "Описание", 30000.0, 10)

    category = Category("Смартфоны", "Описание", [product1, product2])

    assert str(category) == "Смартфоны, количество продуктов: 15 шт."


def test_category_add_product() -> None:
    category = Category("Смартфоны", "Описание", [])

    product = Product("TV", "Описание", 120000.0, 3)
    category.add_product(product)

    assert "TV, 120000 руб. Остаток: 3 шт." in category.products
    assert Category.product_count == 1


def test_category_add_invalid_product() -> None:
    category = Category("Смартфоны", "Описание", [])

    with pytest.raises(TypeError):
        category.add_product("not a product")  # type: ignore


def test_category_without_products() -> None:
    category = Category("Пустая категория", "Без товаров", [])

    assert category.products == "Нет товаров"
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_class_counters_multiple_categories() -> None:
    product1 = Product("Samsung", "Описание", 100000.0, 5)
    product2 = Product("Iphone", "Описание", 200000.0, 7)
    product3 = Product("TV", "Описание", 150000.0, 2)

    Category("Смартфоны", "Описание", [product1, product2])
    Category("Телевизоры", "Описание", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3


# CategoryIterator


def test_category_iterator() -> None:
    product1 = Product("Samsung", "Описание", 100000.0, 5)
    product2 = Product("Iphone", "Описание", 200000.0, 7)

    category = Category("Смартфоны", "Описание", [product1, product2])

    iterator = CategoryIterator(category)
    products = list(iterator)

    assert products == [product1, product2]
