from abc import ABC, abstractmethod


# Forward declaration for type hinting
class Product:
    pass


class Promotion(ABC):
    """
    An abstract base class for different types of promotions.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies the promotion to a given product and quantity.
        Returns the discounted price.
        """
        pass


class PercentageDiscount(Promotion):
    """Applies a percentage-based discount."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if not 0 <= percent <= 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Applies a simple percentage discount."""
        discount_multiplier = 1 - (self.percent / 100)
        return product.price * quantity * discount_multiplier


class SecondHalfPrice(Promotion):
    """Second item is sold at half price."""

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculates the price for a 'second item at half price' deal.
        For every 2 items, one is full price, one is half price.
        """
        num_pairs = quantity // 2
        num_remaining = quantity % 2

        price_of_pairs = num_pairs * (product.price * 1.5)
        price_of_remaining = num_remaining * product.price

        return price_of_pairs + price_of_remaining


class BuyTwoGetOneFree(Promotion):
    """Buy 2 items, get 1 free."""

    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Calculates the price for a 'buy 2, get 1 free' deal.
        For every 3 items, the customer pays for 2.
        """
        num_groups_of_three = quantity // 3
        num_remaining = quantity % 3

        paid_items_count = (num_groups_of_three * 2) + num_remaining

        return paid_items_count * product.price

