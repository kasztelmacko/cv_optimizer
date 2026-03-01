import local_config
from cv_optimizer.pipeline import run
from utils import (
    get_api_key_for_model,
    get_role_name,
    load_json_file,
    output_basename,
    output_folder_name,
)


def main() -> None:
    if local_config.MODEL is None:
        raise ValueError("MODEL is required; set it in local_config.py (e.g. MODEL = 'gemini/gemini-3-flash-preview')")
    role = load_json_file(local_config.ROLE_PATH)
    role_name = get_role_name(role) or ""
    company_name = (role.get("company_name") or "").strip()

    local_config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    folder_name = output_folder_name(role_name, company_name)
    output_dir = local_config.OUTPUT_DIR / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_basename(role_name, company_name)
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
