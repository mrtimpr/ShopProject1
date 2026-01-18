import json
from typing import Any, List

from src.models import Category, Product


def load_categories_from_json(path: str) -> List[Category]:
    """
    Загружает категории и товары из JSON-файла
    и возвращает список объектов Category
    """
    with open(path, "r", encoding="utf-8") as file:
        data: Any = json.load(file)

    categories: List[Category] = []

    if not isinstance(data, list):
        return []

    for category_data in data:
        if not isinstance(category_data, dict):
            continue

        products: List[Product] = []

        raw_products = category_data.get("products", [])
        if isinstance(raw_products, list):
            for product_data in raw_products:
                if not isinstance(product_data, dict):
                    continue

                product = Product(
                    name=str(product_data.get("name", "")),
                    description=str(product_data.get("description", "")),
                    price=float(product_data.get("price", 0.0)),
                    quantity=int(product_data.get("quantity", 0)),
                )
                products.append(product)

        category = Category(
            name=str(category_data.get("name", "")),
            description=str(category_data.get("description", "")),
            products=products,
        )
        categories.append(category)

    return categories
