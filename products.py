from promotions import Promotion

class Product:
    """Represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets the new quantity for the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"

    def set_promotion(self, promotion: Promotion):
        """Sets a promotion for the product."""
        self.promotion = promotion

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of a given quantity of the product.
        Returns the total price of the purchase.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self.quantity < quantity:
            raise Exception(f"Not enough stock for '{self.name}'")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity

class NonStockedProduct(Product):
    """Represents a product that has no quantity and is always available."""
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)  # Quantity is always 0

    def show(self) -> str:
        """Returns a string representation of the non-stocked product."""
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """Processes the purchase of a non-stocked product."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        # No stock check is needed for non-stocked products
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity

class LimitedProduct(Product):
    """Represents a product that has a purchase limit per order."""
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase, enforcing the maximum quantity limit.
        """
        if quantity > self.maximum:
            raise Exception(f"Cannot purchase more than {self.maximum} of '{self.name}'.")
        
        return super().buy(quantity)

