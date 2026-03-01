"""StrEnum classes for JSON personal experience and role keys. One module per JSON file."""

from .personal_experience_enums import (
    EducationKeys,
    PersonalExperienceKeys,
    PersonalProjectKeys,
    ProjectsAndAchievementsKeys,
    WorkExperienceKeys,
    WorkProjectKeys,
)
from .role_description_enums import RoleKeys

__all__ = [
    "EducationKeys",
    "PersonalExperienceKeys",
    "RoleKeys",
    "WorkExperienceKeys",
    "WorkProjectKeys",
    "ProjectsAndAchievementsKeys",
    "PersonalProjectKeys",
]
