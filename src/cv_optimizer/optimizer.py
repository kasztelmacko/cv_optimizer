from langchain_core.messages import HumanMessage, SystemMessage
from langchain_litellm import ChatLiteLLM
from cv_optimizer.prompts import SYSTEM_PROMPT


class CVOptimizer:
    """Produces optimized Work Experience and Projects LaTeX via an LLM."""

    def __init__(
        self,
        model: str,
        api_key: str | None = None,
    ) -> None:
        """Initialize the optimizer with the LLM backend."""
        kwargs: dict[str, str] = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        self._llm = ChatLiteLLM(model=model, **kwargs)

    def optimize(
        self,
        job_description: str,
        md_personal_experience: str,
        current_sections_tex: str | None = None,
        role_name: str | None = None,
    ) -> str:
        """Generate optimized Experience and Projects LaTeX for the given role."""
        role = (role_name.strip() if role_name else "target")
        system_content = SYSTEM_PROMPT.replace("__ROLE_NAME__", role)
        user_parts = [
            "## Job description\n",
            job_description,
            "\n\n## Personal experience (use this to select and rephrase content)\n",
            md_personal_experience,
        ]
        if current_sections_tex:
            user_parts.append("\n\n## Current CV sections (for structure reference)\n")
            user_parts.append(current_sections_tex)
        user_parts.append("\n\nProduce the optimized Work Experience and Projects LaTeX as specified.")

        user_content = "".join(user_parts)
        messages = [
            SystemMessage(content=system_content),
            HumanMessage(content=user_content),
        ]
        response = self._llm.invoke(messages)
        return (response.content or "").strip()
