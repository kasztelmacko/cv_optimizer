"""Run the CV optimizer pipeline. Configure paths and model in local_config.py."""

import local_config
from cv_optimizer.personal_experience_loader import PersonalExperienceLoader
from cv_optimizer.pipeline import run
from utils import get_api_key_for_model


def _output_folder_name(role_name: str, company_name: str) -> str:
    """Build a safe folder name: role_name_company_name."""
    role = (role_name or "role").strip().replace(" ", "_")
    company = (company_name or "company").strip().replace(" ", "_")
    return f"{role}_{company}"


def _output_basename(role_name: str, company_name: str) -> str:
    """Build a safe base name (no extension): role_name_company_name_CV."""
    folder = _output_folder_name(role_name, company_name)
    return f"{folder}_CV"


def main() -> None:
    if local_config.MODEL is None:
        raise ValueError("MODEL is required; set it in local_config.py (e.g. MODEL = 'gemini/gemini-3-flash-preview')")
    loader = PersonalExperienceLoader()
    role = loader.load_role_file(local_config.ROLE_PATH)
    role_name = loader.get_role_name(role) or ""
    company_name = (role.get("company_name") or "").strip()

    local_config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    folder_name = _output_folder_name(role_name, company_name)
    output_dir = local_config.OUTPUT_DIR / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    base = _output_basename(role_name, company_name)
    output_tex = output_dir / f"{base}.tex"

    api_key = get_api_key_for_model(local_config.MODEL)
    run(
        personal_experience_path=local_config.PERSONAL_EXPERIENCE_PATH,
        role_path=local_config.ROLE_PATH,
        template_path=local_config.TEMPLATE_PATH,
        output_path=output_tex,
        model=local_config.MODEL,
        api_key=api_key,
    )
    print(f"Wrote optimized CV to {output_tex} and {output_tex.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
