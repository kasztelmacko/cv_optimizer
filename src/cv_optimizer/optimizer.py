from langchain_core.messages import HumanMessage, SystemMessage
from langchain_litellm import ChatLiteLLM

from cv_optimizer.prompt_loader import PromptLoader


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
        system_content, user_content = PromptLoader().build_cv_optimizer_prompt(
            role_name=role_name,
            job_description=job_description,
            md_personal_experience=md_personal_experience,
            current_sections_tex=current_sections_tex,
        )
        messages = [
            SystemMessage(content=system_content),
            HumanMessage(content=user_content),
        ]
        response = self._llm.invoke(messages)
        return (response.content or "").strip()
