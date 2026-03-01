"""Resolve the API key from .env based on the configured LiteLLM model."""

import os

# Map model prefix to .env variable name
_MODEL_ENV_KEYS = (
    ("gemini/", "GEMINI_API_KEY"),
    ("gemini-", "GEMINI_API_KEY"),
    ("openai/", "OPENAI_API_KEY"),
    ("gpt-", "OPENAI_API_KEY"),
    ("gpt4", "OPENAI_API_KEY"),
)


def get_api_key_for_model(model: str) -> str | None:
    """Return the API key from the environment for the given LiteLLM model string.

    The appropriate env var (e.g. GEMINI_API_KEY, OPENAI_API_KEY) is chosen from
    the model name. Call load_dotenv() before using (e.g. via importing from utils).

    Args:
        model: LiteLLM model string (e.g. "gemini/gemini-3-flash-preview", "gpt-4o-mini").

    Returns:
        The API key if set in .env, else None.
    """
    model_lower = model.lower()
    for prefix, env_var in _MODEL_ENV_KEYS:
        if model_lower.startswith(prefix):
            return os.environ.get(env_var) or None
    return os.environ.get("OPENAI_API_KEY")
