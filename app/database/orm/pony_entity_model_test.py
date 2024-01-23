"""
Pony ORM Entities Module
========================

The `pony_orm_entities` module defines Pony ORM entity classes representing database tables.
Each class corresponds to a specific table in the database and includes attributes mapping to table columns.

Entities
--------
- `User`: Entity representing the 'users' table.
- `Product`: Entity representing the 'products' table.
- `Order`: Entity representing the 'orders' table.
- ... (add more entities as needed)

"""

# Related third-party imports
from pony.orm import Required, Set

# Local module imports
from .pony_orm_connector import PONY_DATABASE


# Define User entity
class User(PONY_DATABASE.Entity):
    """
    User Entity Class

    Represents the 'users' table in the database.

    Attributes
    ----------
    id : int
        Unique identifier for the user.
    username : str
        User's username.
    email : str
        User's email address.
    orders : Set[Order]
        Set of orders associated with the user.

    """

    id = Required(int, auto=True)
    username = Required(str, unique=True)
    email = Required(str, unique=True)
    orders = Set("Order")


# Define Product entity
class Product(PONY_DATABASE.Entity):
    """
    Product Entity Class

    Represents the 'products' table in the database.

    Attributes
    ----------
    id : int
        Unique identifier for the product.
    name : str
        Product name.
    price : float
        Product price.
    orders : Set[Order]
        Set of orders containing the product.

    """

    id = Required(int, auto=True)
    name = Required(str)
    price = Required(float)
    orders = Set("Order")


# Define Order entity
class Order(PONY_DATABASE.Entity):
    """
    Order Entity Class

    Represents the 'orders' table in the database.

    Attributes
    ----------
    id : int
        Unique identifier for the order.
    user : User
        User who placed the order.
    products : Set[Product]
        Set of products included in the order.
    total_price : float
        Total price of the order.

    """

    id = Required(int, auto=True)
    user = Required(User)
    products = Set(Product)
    total_price = Required(float)
