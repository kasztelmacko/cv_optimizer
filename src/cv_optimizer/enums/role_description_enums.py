"""StrEnum classes for all keys in role_description.json."""

from enum import StrEnum


class RoleKeys(StrEnum):
    """Keys in the role description JSON file."""

    ROLE_NAME = "role_name"
    COMPANY_NAME = "company_name"
    JOB_DESCRIPTION = "job_description"
