import json
from pathlib import Path


def load_json_file(path: Path) -> dict:
    """Load and parse a JSON file. Works for both personal experience and role description files."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e


def get_role_name(role: dict) -> str | None:
    """Return the role name from a role dict (e.g. from role_description.json)."""
    name = role.get("role_name")
    return str(name).strip() if name else None


def output_folder_name(role_name: str, company_name: str) -> str:
    """Build a safe folder name: role_name_company_name."""
    role = (role_name or "role").strip().replace(" ", "_")
    company = (company_name or "company").strip().replace(" ", "_")
    return f"{role}_{company}"


def output_basename(role_name: str, company_name: str) -> str:
    """Build a safe base name (no extension): role_name_company_name_CV."""
    folder = output_folder_name(role_name, company_name)
    return f"{folder}_CV"
