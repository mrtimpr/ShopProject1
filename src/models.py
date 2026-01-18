from typing import Dict, Iterator, List


class Product:
    name: str
    description: str
    quantity: int
    __price: float

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            return NotImplemented

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")

        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input("Цена понижается. Вы уверены? (y/n): ")
            if answer.lower() != "y":
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict, products: List["Product"] | None = None) -> "Product":
        """
        Создает новый продукт из словаря.
        При наличии дубликата обновляет количество и цену.
        """
        if products:
            for product in products:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    if product_data["price"] > product.price:
                        product.price = product_data["price"]
                    return product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Category:
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: List[Product]

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает список товаров в виде строки
        """
        if not self.__products:
            return "Нет товаров"

        return "\n".join(str(product) for product in self.__products)

    def get_products(self) -> list[Product]:
        return self.__products


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


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
