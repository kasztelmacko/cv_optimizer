import json
from pathlib import Path

from .enums import (
    EducationKeys,
    PersonalExperienceKeys,
    PersonalProjectKeys,
    ProjectsAndAchievementsKeys,
    RoleKeys,
    WorkExperienceKeys,
    WorkProjectKeys,
)


class PersonalExperienceLoader:
    """Loads personal experience and role data from JSON files for the CV optimization prompt."""

    def load_personal_experience_file(self, personal_experience_path: Path) -> dict:
        """Load and parse the personal experience JSON file."""
        if not personal_experience_path.exists():
            raise FileNotFoundError(f"Personal experience file not found: {personal_experience_path}")
        try:
            return json.loads(personal_experience_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {personal_experience_path}: {e}") from e

    def format_background_for_prompt(self, personal_experience: dict) -> str:
        """Build a single string from education, work_experience, and projects_and_achievements for the LLM."""
        parts: list[str] = []

        if education := personal_experience.get(PersonalExperienceKeys.EDUCATION):
            parts.append("--- Education ---")
            for i, ed in enumerate(education, 1):
                parts.append(f"\n## Degree {i}")
                for key in EducationKeys:
                    if val := ed.get(key):
                        parts.append(f"{key.name.replace('_', ' ').title()}: {val}")
            parts.append("")

        if work := personal_experience.get(PersonalExperienceKeys.WORK_EXPERIENCE):
            parts.append("--- Work Experience ---")
            for emp in work:
                parts.append(f"\n# {emp.get(WorkExperienceKeys.EMPLOYER, '')}")
                parts.append("## General information")
                for key in (WorkExperienceKeys.DURATION, WorkExperienceKeys.LOCATION, WorkExperienceKeys.ROLE_NAME):
                    if val := emp.get(key):
                        parts.append(f"{key.name.replace('_', ' ').title()}: {val}")
                parts.append("\n## Projects:")
                for proj in emp.get(WorkExperienceKeys.PROJECTS) or []:
                    parts.append(f"\n{proj.get(WorkProjectKeys.NAME, '')}:")
                    if proj.get(WorkProjectKeys.OVERVIEW):
                        parts.append(f"Overview: {proj[WorkProjectKeys.OVERVIEW]}")
                    if my_part := proj.get(WorkProjectKeys.MY_PART):
                        parts.append("My part in the project:")
                        for item in my_part:
                            parts.append(f"    - {item}")
                    if proj.get(WorkProjectKeys.PROJECT_IMPACT):
                        parts.append(f"Project impact: {proj[WorkProjectKeys.PROJECT_IMPACT]}")
                    if proj.get(WorkProjectKeys.TOOLS_USED):
                        parts.append(f"Tools used: {proj[WorkProjectKeys.TOOLS_USED]}")
            parts.append("")

        if pa := personal_experience.get(PersonalExperienceKeys.PROJECTS_AND_ACHIEVEMENTS):
            if personal := pa.get(ProjectsAndAchievementsKeys.PERSONAL_PROJECTS):
                parts.append("--- Personal projects ---")
                for p in personal:
                    parts.append(f"\n## {p.get(PersonalProjectKeys.NAME, '')}")
                    if p.get(PersonalProjectKeys.OVERVIEW):
                        parts.append(f"Overview: {p[PersonalProjectKeys.OVERVIEW]}")
                    if p.get(PersonalProjectKeys.TOOLS):
                        parts.append(f"Tools: {p[PersonalProjectKeys.TOOLS]}")
                    if p.get(PersonalProjectKeys.GITHUB):
                        parts.append(f"Github: {p[PersonalProjectKeys.GITHUB]}")
                parts.append("")
            if achievements := pa.get(ProjectsAndAchievementsKeys.ACHIEVEMENTS):
                parts.append("--- Achievements ---")
                for a in achievements:
                    parts.append(f"\n## {a.get(PersonalProjectKeys.NAME, '')}")
                    if a.get(PersonalProjectKeys.OVERVIEW):
                        parts.append(f"Overview: {a[PersonalProjectKeys.OVERVIEW]}")
                    if a.get(PersonalProjectKeys.TOOLS):
                        parts.append(f"Tools: {a[PersonalProjectKeys.TOOLS]}")
                    if a.get(PersonalProjectKeys.GITHUB):
                        parts.append(f"Github: {a[PersonalProjectKeys.GITHUB]}")

        return "\n".join(parts).strip()

    def load_role_file(self, role_path: Path) -> dict:
        """Load and parse the role description JSON file."""
        if not role_path.exists():
            raise FileNotFoundError(f"Role file not found: {role_path}")
        try:
            return json.loads(role_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {role_path}: {e}") from e

    def get_job_description(self, role: dict) -> str:
        """Return the full job description text from the role dict.

        Combines role_name, company_name, and job_description for the prompt.
        """
        role_name = role.get(RoleKeys.ROLE_NAME, "")
        company = role.get(RoleKeys.COMPANY_NAME, "")
        desc = (role.get(RoleKeys.JOB_DESCRIPTION) or "").strip()
        bits = []
        if role_name:
            bits.append(f"Role name: {role_name}")
        if company:
            bits.append(f"Company name: {company}")
        if desc:
            bits.append(f"Job description:\n{desc}")
        return "\n".join(bits).strip() if bits else ""

    def get_role_name(self, role: dict) -> str | None:
        """Return the role name from the role dict if present."""
        name = role.get(RoleKeys.ROLE_NAME)
        return str(name).strip() if name else None
