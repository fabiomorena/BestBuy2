

Best Buy CLI Store Simulation
This project is a simple, object-oriented command-line simulation of a retail store like Best Buy. It manages products, inventory, and various promotional discounts. The entire application is written in Python and includes a comprehensive test suite using pytest.

Features
Product Management: Create products with a name, price, and quantity. Products can be activated, deactivated, and tracked.

Store Inventory: The Store class holds a list of all products, can add or remove products, and provides a total inventory count.

Order Processing: A robust order method that processes a shopping list, updates product quantities, and calculates the total cost.

Promotions System: An abstract Promotion class allows for flexible promotional deals, including:

Percentage-based discounts

"Second Item Half Price" deals

"Buy Two, Get One Free" offers

Comprehensive Testing: Includes a full suite of unit tests written with pytest to ensure all classes and methods work as expected.

Project Structure
BestBuy2/
│
├── .gitignore
├── main.py             # Pytest tests for the Store class
├── products.py         # Contains the Product class
├── promotions.py       # Contains all Promotion classes
├── store.py            # Contains the Store class
└── test_products.py    # Pytest tests for the Product class
Getting Started
Prerequisites
Python 3.x

pytest library

Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/BestBuy2.git
cd BestBuy2
Install dependencies:
It is recommended to use a virtual environment.

Bash

# Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install pytest
pip install pytest
Running the Tests
To ensure everything is working correctly, run the test suite from the project's root directory:

Bash

pytest
All tests for both the Product and Store classes should pass.

How It Works
The simulation is built around two main classes: Product and Store.

Product: Each instance represents a unique item in the store. It manages its own quantity and can have a promotion applied to it. When an item is purchased, the buy method calculates the cost (applying any promotions) and updates its own stock level.

Store: This class manages the collection of all Product instances. It can add, remove, and list products. The order method takes a shopping list (product, quantity) and processes the entire transaction, returning the total cost.
