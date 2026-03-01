"""Shared utilities for the CV optimizer."""

from dotenv import load_dotenv

from .api_key import get_api_key_for_model

# Load .env on first import so API keys are available
load_dotenv()

__all__ = ["get_api_key_for_model"]
