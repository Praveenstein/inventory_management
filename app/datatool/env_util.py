"""
Environment Variable Utility
===========================

This module provides utilities for retrieving and validating environment variables using Pydantic.

Functions
---------
get_settings: Retrieve an environment variables with optional default value.


classes
-------
Setting : BaseSettings
    A class for handling environment variable.
"""

# Standard library imports
import logging
from functools import lru_cache

# Related third party imports
from pydantic_settings import BaseSettings


__author__ = "Praveen Kumar G"

LOGGER = logging.getLogger(__name__)


class EnvironmentVariable(BaseSettings):
    """Data model for configuration settings."""

    # Database provider (postgres, sqlite, etc.)
    timescaledb_provider: str

    # Database user
    timescaledb_user: str

    # Database password for user
    timescaledb_password: str

    # Database host identifier
    timescaledb_host: str

    # Database name (within postgresql)
    timescaledb_database: str

    # Default Logging configuration file path
    logger_configuration_file: str

    class Config:
        env_file = "./config/.env"


@lru_cache()
def get_env_variables():
    """
    Return the configuration settings read from the os environment, using pydantic's base settings class

    Returns
    -------
    EnvironmentVariable
        The configuration settings read from the os
    """

    LOGGER.debug("New Request for environment variable")
    return EnvironmentVariable()
