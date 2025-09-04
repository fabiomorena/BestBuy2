import pytest
from products import Product
from promotions import PercentageDiscount, SecondHalfPrice, BuyTwoGetOneFree

def test_create_product():
    """Test that a product is created with the correct attributes."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True

def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", price=100, quantity=10)
    with pytest.raises(ValueError, match="Price and quantity cannot be negative."):
        Product("Invalid", price=-100, quantity=10)

def test_product_becomes_inactive_at_zero_quantity():
    """Test that a product becomes inactive when its quantity reaches zero."""
    product = Product("Test Item", price=10, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert product.is_active() is False

def test_buy_modifies_quantity_and_returns_right_price():
    """Test that buying a product correctly modifies its quantity and returns the correct price."""
    product = Product("Test Item", price=10, quantity=10)
    total_price = product.buy(3)
    assert product.get_quantity() == 7
    assert total_price == 30.0

def test_buy_too_much_raises_exception():
    """Test that buying more than the available quantity raises an exception."""
    product = Product("Test Item", price=10, quantity=5)
    with pytest.raises(Exception, match="Not enough stock for 'Test Item'"):
        product.buy(6)

def test_set_promotion():
    """Test that a promotion can be set for a product."""
    product = Product("Test Item", price=10, quantity=10)
    promo = PercentageDiscount("Sale", 20)
    product.set_promotion(promo)
    assert product.promotion is promo

def test_buy_with_percentage_discount():
    """Test buying a product with a percentage discount."""
    product = Product("Bose Headphones", price=250, quantity=20)
    product.set_promotion(PercentageDiscount("Clearance", 30))
    total_price = product.buy(1)
    assert total_price == 175.0  # 30% off 250

def test_buy_with_second_half_price():
    """Test buying products with a 'second half price' promotion."""
    product = Product("Earbuds", price=100, quantity=10)
    product.set_promotion(SecondHalfPrice("2nd Half Price"))
    # Test with an even number
    total_price_even = product.buy(2)
    assert total_price_even == 150.0
    # Test with an odd number
    product.set_quantity(10) # Reset quantity
    total_price_odd = product.buy(3)
    assert total_price_odd == 250.0

def test_buy_with_buy_two_get_one_free():
    """Test buying products with a 'buy 2, get 1 free' promotion."""
    product = Product("Google Pixel", price=500, quantity=10)
    product.set_promotion(BuyTwoGetOneFree("B2G1 Free"))
    # Test with a multiple of 3
    total_price_multiple = product.buy(3)
    assert total_price_multiple == 1000.0
    # Test with a non-multiple
    product.set_quantity(10) # Reset quantity
    total_price_non_multiple = product.buy(4)
    assert total_price_non_multiple == 1500.0
