"""
Pony ORM Connector Module
========================

The `pony_orm_connector` module provides functions for initializing and configuring the Pony ORM connector.
It includes functionality to set up a Pony ORM database connection, generate mapping, and enable SQL debugging.

Functions
---------
- `initialize_pony`: Function to initialize the Pony ORM database connection and configure settings.

Usage
-----
Import this module and use the `initialize_pony` function to set up your Pony ORM database connection.

"""

# Standard library imports
import logging

# Related third-party imports
from pony.orm import Database, set_sql_debug

# Local module imports
from app.datatool.env_util import get_env_variables

__author__ = "smt18m005@iiitdm.ac.in"

LOGGER = logging.getLogger(__name__)

PONY_DATABASE = Database()


def initialize_pony(debug=False):
    """
    Initialize Pony ORM Database Connection.

    Parameters
    ----------
    debug : bool, optional
        Enable or disable SQL debugging (default is True).

    Returns
    -------
    None

    """
    env_variables = get_env_variables()

    LOGGER.info(env_variables.timescaledb_provider)
    LOGGER.info(env_variables.timescaledb_user)
    LOGGER.info(env_variables.timescaledb_password)
    LOGGER.info(env_variables.timescaledb_host)
    LOGGER.info(env_variables.timescaledb_database)
    PONY_DATABASE.bind(provider=env_variables.timescaledb_provider, user=env_variables.timescaledb_user,
                       password=env_variables.timescaledb_password, host=env_variables.timescaledb_host,
                       database=env_variables.timescaledb_database)

    LOGGER.info("Database Bound to Given Credentials")
    if debug:
        set_sql_debug(True)
