import products
from typing import List, Tuple


class Store:
    """
    Represents a store that holds a list of products and can process orders.
    """

    def __init__(self, list_of_products: List[products.Product]):
        """Initializes a Store instance with a list of products."""
        self.products = list_of_products if list_of_products else []

    def add_product(self, product: products.Product):
        """Adds a product to the store's inventory."""
        self.products.append(product)

    def remove_product(self, product: products.Product):
        """Removes a product from the store's inventory."""
        if product in self.products:
            self.products.remove(product)
        else:
            print(f"Error: Product {product.name} not found in store.")

    def get_total_quantity(self) -> int:
        """Returns the total count of all items in the store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[products.Product, int]]) -> float:
        """
        Processes an order from a shopping list.
        The shopping list is a list of (product, quantity) tuples.
        Returns the total cost of the order.
        """
        total_cost = 0.0
        for product_to_buy, quantity in shopping_list:
            try:
                # The product's 'buy' method handles stock checks and exceptions
                item_cost = product_to_buy.buy(quantity)
                total_cost += item_cost
            except Exception as e:
                print(f"Order failed for {product_to_buy.name}: {e}")
                # In a real-world scenario, you might implement transaction
                # logic to roll back the entire order if one item fails.
                # For this exercise, we let the exception halt the process.
                raise
        return total_cost
