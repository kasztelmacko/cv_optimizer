from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PERSONAL_EXPERIENCE_PATH = PROJECT_ROOT / "context" / "personal_experience.json"
ROLE_PATH = PROJECT_ROOT / "context" / "role_description.json"

TEMPLATE_PATH = PROJECT_ROOT / "context" / "current_cv.tex"
OUTPUT_DIR = PROJECT_ROOT / "output_cv"
MODEL = "gemini/gemini-3-flash-preview"
