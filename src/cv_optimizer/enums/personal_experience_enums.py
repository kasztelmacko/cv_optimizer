"""StrEnum classes for all keys in personal_experience.json."""

from enum import StrEnum


class PersonalExperienceKeys(StrEnum):
    """Top-level keys in the personal experience JSON file."""

    EDUCATION = "education"
    WORK_EXPERIENCE = "work_experience"
    PROJECTS_AND_ACHIEVEMENTS = "projects_and_achievements"


class EducationKeys(StrEnum):
    """Keys for each education entry."""

    DEGREE = "degree"
    UNIVERSITY = "university"
    GRADUATION_DATE = "graduation_date"
    THESIS_TOPIC = "thesis_topic"
    OVERVIEW = "overview"
    TOOLS = "tools"


class WorkExperienceKeys(StrEnum):
    """Keys for each work experience (employer) entry."""

    EMPLOYER = "employer"
    DURATION = "duration"
    LOCATION = "location"
    ROLE_NAME = "role_name"
    PROJECTS = "projects"


class WorkProjectKeys(StrEnum):
    """Keys for each project under a work experience entry."""

    NAME = "name"
    OVERVIEW = "overview"
    MY_PART = "my_part"
    PROJECT_IMPACT = "project_impact"
    TOOLS_USED = "tools_used"


class ProjectsAndAchievementsKeys(StrEnum):
    """Top-level keys under projects_and_achievements."""

    PERSONAL_PROJECTS = "personal_projects"
    ACHIEVEMENTS = "achievements"


class PersonalProjectKeys(StrEnum):
    """Keys for each personal project or achievement entry."""

    NAME = "name"
    OVERVIEW = "overview"
    TOOLS = "tools"
    GITHUB = "github"
