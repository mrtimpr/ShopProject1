from abc import ABC, abstractmethod


class BaseProduct(ABC):
    name: str
    description: str
    quantity: int

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: object) -> float:
        pass


class BaseEntity(ABC):
    @abstractmethod
    def total_price(self) -> None:
        pass
