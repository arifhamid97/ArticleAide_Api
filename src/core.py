from enum import Enum
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


load_dotenv()


class PromptFlavour(Enum):
    ANALOGY = "ANALOGY"
    HIGHSCHOOL = "HIGHSCHOOL"
    GENERAL = "GENERAL"

    @staticmethod
    def get_prompt_flavour(flavour: "PromptFlavour") -> str:
        switcher = {
            PromptFlavour.ANALOGY: "By giving a real-life analogy.",
            PromptFlavour.HIGHSCHOOL: "like I am a highschool student",
            PromptFlavour.GENERAL: "",
        }
        return switcher.get(flavour)


class Result(BaseModel):
    explaination: str = Field(description="Answer for the explanation")


class Model:
    def __init__(self) -> None:
        self.open_ai_key = os.getenv("OPENAI_API_KEY")
        self.open_model = os.getenv("OPENAI_MODEL")

    def __init_open_ai(self):
        model = ChatOpenAI(openai_api_key=self.open_ai_key, model=self.open_model)
        return model

    def debug_invoke_chain(self, context: str, flavour: PromptFlavour):

        template = """
        explain {context} {flavour_template}
        {format_instructions}
        """
        parser = JsonOutputParser(pydantic_object=Result)

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "flavour_template"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        formatted_prompt = prompt.format(
            context=context, flavour_template=PromptFlavour.get_prompt_flavour(flavour)
        )
        print("formtted input: ", formatted_prompt)

    def invoke_chain(self, context: str, flavour: PromptFlavour):

        template = """
        explain {context} {flavour_template}
        {format_instructions}
        """
        parser = JsonOutputParser(pydantic_object=Result)

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "flavour_template"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        model = self.__init_open_ai()

        chain = prompt | model | parser
        return chain.invoke(
            {
                "context": context,
                "flavour_template": PromptFlavour.get_prompt_flavour(flavour),
            }
        )
