import local_config
from cv_optimizer.pipeline import run
from utils import (
    get_api_key_for_model,
    output_basename,
    output_folder_name,
    save_json_file,
)


def main() -> None:
    if local_config.MODEL is None:
        raise ValueError("MODEL is required; set it in local_config.py (e.g. MODEL = 'gemini/gemini-3-flash-preview')")

    role_name = (local_config.ROLE_NAME or "").strip()
    company_name = (local_config.COMPANY_NAME or "").strip()
    role = {
        "role_name": role_name or None,
        "company_name": company_name or None,
        "job_description": (local_config.JOB_DESCRIPTION or "").strip() or None,
    }

    local_config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    folder_name = output_folder_name(role_name, company_name)
    output_dir = local_config.OUTPUT_DIR / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    role_description_path = output_dir / "role_description.json"
    save_json_file(role_description_path, role)

    base = output_basename(role_name, company_name)
    output_tex = output_dir / f"{base}.tex"

    api_key = get_api_key_for_model(local_config.MODEL)
    run(
        personal_experience_path=local_config.PERSONAL_EXPERIENCE_PATH,
        role_path=role_description_path,
        template_path=local_config.TEMPLATE_PATH,
        output_path=output_tex,
        model=local_config.MODEL,
        api_key=api_key,
    )
    print(f"Wrote optimized CV to {output_tex} and {output_tex.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
