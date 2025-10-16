"""
Common tools and utilities for ADK examples.

These functions provide shared functionality that can be used across
different examples to reduce code duplication and ensure consistency.
"""

import os
import sys
import logging
from typing import Optional, Any, Dict
from functools import wraps


def get_env_var(var_name: str, default: Optional[str] = None, required: bool = False) -> Optional[str]:
    """
    Get an environment variable with optional default and validation.

    Args:
        var_name: Name of the environment variable
        default: Default value if not found
        required: If True, raises error when not found and no default

    Returns:
        The environment variable value or default

    Raises:
        ValueError: If required and not found
    """
    value = os.getenv(var_name, default)

    if required and value is None:
        raise ValueError(
            f"Required environment variable '{var_name}' not found. "
            f"Please set it in your .env file."
        )

    return value


def setup_logging(name: str = "adk_example", level: str = "INFO") -> logging.Logger:
    """
    Set up a configured logger for an example.

    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Only add handler if logger doesn't have one
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(getattr(logging, level.upper()))
    return logger


def validate_api_key(api_key: Optional[str], provider: str = "Google") -> bool:
    """
    Basic validation for API keys.

    Args:
        api_key: The API key to validate
        provider: The provider name for error messages

    Returns:
        True if valid, False otherwise
    """
    if not api_key:
        print(f"❌ No {provider} API key found. Please set it in your .env file.")
        return False

    if api_key == f"your-{provider.lower()}-api-key-here" or api_key.startswith("your-"):
        print(f"❌ Please replace the placeholder {provider} API key in your .env file.")
        return False

    if len(api_key) < 10:
        print(f"❌ {provider} API key seems too short. Please check your .env file.")
        return False

    return True


def format_response(response: Any, max_length: int = 500) -> str:
    """
    Format an agent response for display.

    Args:
        response: The response to format
        max_length: Maximum length before truncation

    Returns:
        Formatted string representation
    """
    if response is None:
        return "No response received"

    response_str = str(response)

    if len(response_str) > max_length:
        return f"{response_str[:max_length]}... (truncated)"

    return response_str


def handle_error(func):
    """
    Decorator for handling common errors in examples.

    Provides user-friendly error messages for common issues.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ImportError as e:
            print(f"❌ Import Error: {e}")
            print("💡 Tip: Make sure you have installed all requirements:")
            print("   pip install google-adk")
            sys.exit(1)
        except ValueError as e:
            if "API" in str(e) or "key" in str(e).lower():
                print(f"❌ Configuration Error: {e}")
                print("💡 Tip: Check your .env file and ensure all required keys are set")
            else:
                print(f"❌ Value Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            print("💡 Tip: Check the example README for troubleshooting steps")
            sys.exit(1)

    return wrapper


def load_example_config(example_name: str) -> Dict[str, Any]:
    """
    Load configuration for a specific example.

    Args:
        example_name: Name of the example

    Returns:
        Configuration dictionary
    """
    config = {
        "name": example_name,
        "model": get_env_var("DEFAULT_MODEL", "gemini-2.5-flash"),
        "temperature": float(get_env_var("DEFAULT_TEMPERATURE", "0.7")),
        "max_tokens": int(get_env_var("MAX_OUTPUT_TOKENS", "2048")),
    }

    # Load example-specific overrides if they exist
    example_model = get_env_var(f"{example_name.upper()}_MODEL")
    if example_model:
        config["model"] = example_model

    return config


# Common prompt templates that can be reused
PROMPT_TEMPLATES = {
    "helpful_assistant": "You are a helpful assistant. Answer questions clearly and concisely.",

    "technical_expert": "You are a technical expert. Provide detailed, accurate technical information.",

    "creative_writer": "You are a creative writer. Generate engaging and imaginative content.",

    "data_analyst": "You are a data analyst. Analyze information and provide insights based on data.",

    "customer_support": "You are a friendly customer support agent. Help users with their questions and issues.",
}


def get_prompt_template(template_name: str) -> str:
    """
    Get a common prompt template.

    Args:
        template_name: Name of the template

    Returns:
        The prompt template string
    """
    return PROMPT_TEMPLATES.get(
        template_name,
        PROMPT_TEMPLATES["helpful_assistant"]
    )