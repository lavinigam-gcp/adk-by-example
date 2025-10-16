"""
Shared utilities for ADK by Example.

This module contains common functions and tools that can be used across examples.
"""

from .common_tools import (
    get_env_var,
    setup_logging,
    validate_api_key,
    format_response,
    handle_error
)

__all__ = [
    'get_env_var',
    'setup_logging',
    'validate_api_key',
    'format_response',
    'handle_error'
]