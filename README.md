# CV Optimizer

Optimize your CV for a given role using personal experience and role (JSON files) and an LLM (LiteLLM + LangChain). The tool rewrites only the Work Experience and Projects sections in LaTeX and assembles a complete CV.

## Setup

- Python 3.12+, [uv](https://docs.astral.sh/uv/)
- Copy `.env.example` to `.env` and set your API key:
  ```
  LLM_API_KEY=your-api-key-here
  ```

```bash
uv sync
```

## Usage

Set all paths and options in **local_config.py**, then run:

```bash
uv run python main.py
```

The optimized CV is written to **output_cv/** as `{role_name}_{company_name}_CV.tex` (spaces trimmed and replaced with underscores for a valid path). Example: `Data_Scientist_Allegro_CV.tex`.

## Configuration (local_config.py)

- **PERSONAL_EXPERIENCE_PATH** — personal experience JSON (education, work experience, projects).
- **ROLE_PATH** — role description JSON (role_name, company_name, job_description).
- **TEMPLATE_PATH** — current CV LaTeX template.
- **OUTPUT_DIR** — directory for generated CVs (default: `output_cv`).
- **MODEL** — LiteLLM model string (e.g. `gpt-4o-mini`).

## Input files

- **context/personal_experience.json** — your background: `education`, `work_experience`, `projects_and_achievements`.
- **context/role_description.json** — target role: `role_name`, `company_name`, `job_description`.

Your current CV LaTeX is at `context/current_cv.tex`.
