from pathlib import Path


MARKER_EXPERIENCE_START = "%-----------Experience---------------"
MARKER_SKILLS_START = "%-----------PROGRAMMING SKILLS-----------"


class CVTemplate:
    """Holds the current CV .tex and exposes header/footer for injecting optimized sections."""

    def __init__(self, tex_path: Path) -> None:
        """Load the template and split into header, replaceable block, and footer."""
        if not tex_path.exists():
            raise FileNotFoundError(f"Template file not found: {tex_path}")

        self._tex_path = tex_path
        content = tex_path.read_text(encoding="utf-8")

        if MARKER_EXPERIENCE_START not in content:
            raise ValueError(
                f"Template missing Experience marker: {MARKER_EXPERIENCE_START!r}"
            )
        if MARKER_SKILLS_START not in content:
            raise ValueError(
                f"Template missing Technical Skills marker: {MARKER_SKILLS_START!r}"
            )

        start_idx = content.index(MARKER_EXPERIENCE_START)
        end_idx = content.index(MARKER_SKILLS_START)

        self._header = content[:start_idx].rstrip()
        self._footer = content[end_idx:].rstrip()
        self._experience_and_projects = content[start_idx:end_idx].rstrip()

    @property
    def experience_and_projects_tex(self) -> str:
        """Current Experience + Projects LaTeX block (for prompt context)."""
        return self._experience_and_projects

    def assemble(self, experience_and_projects_tex: str) -> str:
        """Build the full .tex document with the given Experience and Projects block."""
        return (
            f"{self._header}\n\n"
            f"{experience_and_projects_tex.strip()}\n\n"
            f"{self._footer}\n"
        )
