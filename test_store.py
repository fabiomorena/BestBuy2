import pytest
from store import Store
from products import Product


@pytest.fixture
def setup_store():
    """Fixture to create a store with some products for testing."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=10),
        Product("Bose QuietComfort Earbuds", price=250, quantity=20),
        Product("Google Pixel 7", price=500, quantity=15),
    ]
    return Store(product_list)


def test_add_product(setup_store):
    """Test that adding a product increases the store's product count."""
    store = setup_store
    initial_product_count = len(store.get_all_products())
    new_product = Product("Sony WH-1000XM5", price=400, quantity=30)
    store.add_product(new_product)
    assert len(store.get_all_products()) == initial_product_count + 1


def test_remove_product(setup_store):
    """Test that removing a product decreases the store's product count."""
    store = setup_store
    initial_product_count = len(store.get_all_products())
    product_to_remove = store.get_all_products()[0]
    store.remove_product(product_to_remove)
    assert len(store.get_all_products()) == initial_product_count - 1


def test_get_total_quantity(setup_store):
    """Test that the total quantity of all items in the store is correct."""
    store = setup_store
    assert store.get_total_quantity() == 45


def test_get_all_products(setup_store):
    """Test that all active products in the store are returned."""
    store = setup_store
    all_products = store.get_all_products()
    assert len(all_products) == 3


def test_order_successful(setup_store):
    """Test that a valid order is processed correctly."""
    store = setup_store
    products_to_order = store.get_all_products()
    order_list = [(products_to_order[0], 1), (products_to_order[1], 2)]
    total_cost = store.order(order_list)
    assert total_cost == 1950.0
    assert products_to_order[0].get_quantity() == 9
    assert products_to_order[1].get_quantity() == 18


def test_order_insufficient_stock(setup_store):
    """Test that an order with insufficient stock raises an exception."""
    store = setup_store
    products_to_order = store.get_all_products()
    order_list = [(products_to_order[0], 11)]  # Requesting more than available
    with pytest.raises(Exception, match="Not enough stock for 'MacBook Air M2'"):
        store.order(order_list)
      
