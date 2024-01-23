"""
ORM Create Operation Module
===========================

The `create_operation` module within the `orm` subpackage provides functions to create records in the database
using Object-Relational Mapping (ORM) tools. It includes functionalities to insert new records into the database
tables represented by ORM entities.

Functions
---------
- `insert_movies_data`: Function to insert movie records in the database from a given list of data.
- `create_product_record`: Function to create a new product record in the database.
- `create_order_record`: Function to create a new order record in the database.
- ... (add more functions as needed)

"""

# Standard library imports
import logging
import time

# Related third-party imports
from pony.orm import db_session

# Local module imports
import app.database.orm.pony_entity_model as pony_models


LOGGER = logging.getLogger(__name__)


@db_session
def insert_movies_data(data: list[list]):
    LOGGER.debug("Inserting Movies")
    # for movie in data:
    #     pony_models.Movie(title=movie[0], director=movie[1],
    #                       year=movie[2], length_minutes=movie[3])

    for _ in range(10000):
        pony_models.Movie(title="title_" + str(_), director="director_" + str(_),
                          year=_, length_minutes=_)


def main():
    data = [
        ["Toy Story", "John Lasseter", 1995, 81],
        ["A Bug's Life", "John Lasseter", 1998, 95],
        ["Toy Story 2", "John Lasseter", 1999, 93],
        ["Monsters, Inc.", "Pete Docter", 2001, 92],
        ["Finding Nemo", "Andrew Stanton", 2003, 107],
        ["The Incredibles", "Brad Bird", 2004, 116],
        ["Cars", "John Lasseter", 2006, 117],
        ["Ratatouille", "Brad Bird", 2007, 115],
        ["WALL-E", "Andrew Stanton", 2008, 104],
        ["Up", "Pete Docter", 2009, 101],
        ["Toy Story 3", "Lee Unkrich", 2010, 103],
        ["Cars 2", "John Lasseter", 2011, 120],
        ["Brave", "Brenda Chapman", 2012, 102],
        ["Monsters University", "Dan Scanlon", 2013, 110],
    ]

    start_time = time.time()  # Record the start time

    insert_movies_data(data)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time

    LOGGER.info(f"Inserted Movies in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
