from typing import Iterator, List

from src.exceptions import ZeroQuantityError

from .product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: List[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты или их наследников")

        try:
            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством")

            self.__products.append(product)
            Category.product_count += 1
        except ZeroQuantityError as e:
            print(e)
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        if not self.__products:
            return "Нет товаров"

        return "\n".join(str(product) for product in self.__products)

    def get_products(self) -> List[Product]:
        return self.__products

    def average_price(self) -> float:
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self._products = category.get_products()
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        return self

    def __next__(self) -> Product:
        if self._index >= len(self._products):
            raise StopIteration

        product = self._products[self._index]
        self._index += 1
        return product
