from pydantic import BaseModel, field_validator
from src.core import PromptFlavour


class Query(BaseModel):
    context: str
    prompt_flavour: PromptFlavour

    @field_validator("prompt_flavour", mode="before")
    def validate_prompt_flavour(cls, value):
        if isinstance(value, str):
            try:
                return PromptFlavour(
                    value
                )  # Validate if the string is a valid enum member
            except ValueError:
                raise ValueError(f"Invalid value for PromptFlavour: {value}")
        raise ValueError("prompt_flavour must be a string")
