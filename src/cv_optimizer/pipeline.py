import subprocess
from pathlib import Path

from utils import get_role_name, load_json_file

from .cv_template import CVTemplate
from .optimizer import CVOptimizer
from .prompt_loader import PromptLoader


def _clean_auxiliary_files(tex_path: Path) -> None:
    """Remove LaTeX auxiliary files (.aux, .log, .out) for the given .tex file."""
    for ext in (".aux", ".log", ".out"):
        aux_file = tex_path.with_suffix(ext)
        if aux_file.exists():
            aux_file.unlink()


def compile_tex_to_pdf(tex_path: Path) -> Path:
    """Run pdflatex on the .tex file and return the path to the generated .pdf.

    Runs pdflatex twice so references resolve. Requires a LaTeX distribution (e.g. MiKTeX, TeX Live).
    Removes auxiliary files (.aux, .log, .out) after a successful build so only .tex and .pdf remain.
    """
    if not tex_path.exists():
        raise FileNotFoundError(f"Cannot compile: {tex_path} not found")
    out_dir = tex_path.parent
    cmd = ["pdflatex", "-interaction=nonstopmode", tex_path.name]
    for _ in range(2):
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=out_dir,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"pdflatex failed (exit {result.returncode}). stderr: {result.stderr or result.stdout}"
            )
    pdf_path = tex_path.with_suffix(".pdf")
    if not pdf_path.exists():
        raise RuntimeError(f"pdflatex did not produce {pdf_path}")
    _clean_auxiliary_files(tex_path)
    return pdf_path


def run(
    personal_experience_path: Path,
    role_path: Path,
    template_path: Path | None = None,
    output_path: Path | None = None,
    model: str | None = None,
    api_key: str | None = None,
) -> None:
    """Load personal experience and role from JSON, run the optimizer, then write .tex and compile to .pdf in one step."""
    if output_path is None:
        raise ValueError("output_path is required")
    if model is None:
        raise ValueError("model is required; set MODEL in local_config.py")

    if template_path is None:
        template_path = personal_experience_path.parent / "current_cv.tex"

    personal_experience = load_json_file(personal_experience_path)
    role = load_json_file(role_path)
    loader = PromptLoader()
    md_personal_experience = loader.format_background_for_prompt(personal_experience)
    job_description = loader.get_job_description(role)
    role_name = get_role_name(role)

    template = CVTemplate(template_path)
    optimizer = CVOptimizer(model=model, api_key=api_key)
    experience_and_projects_tex = optimizer.optimize(
        job_description=job_description,
        md_personal_experience=md_personal_experience,
        current_sections_tex=template.experience_and_projects_tex,
        role_name=role_name,
    )
    full_tex = template.assemble(experience_and_projects_tex)
    output_path.write_text(full_tex, encoding="utf-8")
    compile_tex_to_pdf(output_path)
