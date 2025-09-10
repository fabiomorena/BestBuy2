import products
import promotions
import store

def start(best_buy):
    """
    Starts the command-line interface for the Best Buy store.
    """
    while True:
        print("\n-----------")
        print("Best Buy Menu")
        print("-----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == '1':
            list_products(best_buy)
        elif choice == '2':
            show_total_quantity(best_buy)
        elif choice == '3':
            make_order(best_buy)
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def list_products(best_buy):
    """Lists all active products in the store."""
    print("\n--- Available Products ---")
    all_products = best_buy.get_all_products()
    for i, product in enumerate(all_products, 1):
        print(f"{i}. {product.show()}")

def show_total_quantity(best_buy):
    """Shows the total quantity of all items in the store."""
    total_quantity = best_buy.get_total_quantity()
    print(f"\nTotal items in store: {total_quantity}")

def make_order(best_buy):
    """Handles the process of making an order."""
    all_products = best_buy.get_all_products()
    if not all_products:
        print("Sorry, there are no products to order.")
        return

    list_products(best_buy)
    shopping_list = []

    while True:
        try:
            product_choice = input("Which product # do you want? (or 'done' to finish): ")
            if product_choice.lower() == 'done':
                break

            product_index = int(product_choice) - 1
            if not 0 <= product_index < len(all_products):
                print("Error: Invalid product number.")
                continue

            chosen_product = all_products[product_index]

            quantity_choice = input(f"What amount of {chosen_product.name} do you want?: ")
            quantity = int(quantity_choice)

            shopping_list.append((chosen_product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    if shopping_list:
        try:
            total_cost = best_buy.order(shopping_list)
            print(f"\nOrder successful! Total cost: ${total_cost:.2f}")
        except Exception as e:
            print(f"\nCould not complete the order. Reason: {e}")

def main():
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    buy_two_get_one_free = promotions.BuyTwoGetOneFree("Buy Two Get One Free!")
    thirty_percent = promotions.PercentageDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(buy_two_get_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
