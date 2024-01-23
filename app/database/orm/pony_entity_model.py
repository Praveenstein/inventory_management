"""
Pony ORM Entities Module
========================

The `pony_orm_entities` module defines Pony ORM entity classes representing database tables.
Each class corresponds to a specific table in the database and includes attributes mapping to table columns.

Entities
--------
- `Movie`: Entity representing the 'Movies' table.

"""

# Standard library imports
import logging

# Related third-party imports
from pony.orm import Required, Set, PrimaryKey

# Local module imports
from .pony_orm_connector import PONY_DATABASE


LOGGER = logging.getLogger(__name__)


# Define Movie Entity
class Movie(PONY_DATABASE.Entity):

    _table_ = ("revision", "Movies")
    id = PrimaryKey(int, auto=True, column="Id")
    title = Required(str, column="Title", index=True)
    director = Required(str, column="Director")
    year = Required(int, column="Year")
    length_minutes = Required(int, column="Length_minutes")


def generate_pony_mapping(create_tables=False):
    """
    Generate Pony ORM Database Mapping to Entities.

    Parameters
    ----------
    create_tables : bool, optional
        Enable or disable creating table if it does not exist.

    Returns
    -------
    None

    """
    PONY_DATABASE.generate_mapping(create_tables=create_tables)
    LOGGER.info("Generated Mapping")
