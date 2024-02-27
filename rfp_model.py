import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

class OpenAILLM:
    def __init__(self):
        self.OpenAIGPT4 = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'],
                                     model_name="gpt-4", temperature=0.1)
