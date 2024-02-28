import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

class ChatModel:
    def __init__(self):
        #self.OpenAIGPT4 = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'], model_name="gpt-4", temperature=0.1)
        self.localMistral = ChatOpenAI(base_url=os.environ['MISTRAL_API_BASE'],
                                       model_name=os.environ['MISTRAL_MODEL_NAME'])