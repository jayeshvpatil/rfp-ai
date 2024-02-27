import os
from textwrap import dedent
from crewai import Agent
from tools.ExaSearchTool import ExaSearchTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

class RFPAgents:
	def __init__(self):
		load_dotenv()
		self.OpenAIGPT4 = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'],
                                     model_name="gpt-4", temperature=0.1)

	def industry_analysis_agent(self):
		return Agent(
			role='Industry Analyst',
			goal='Analyze the current industry trends, challenges, and opportunities',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a Analyst, your analysis will identify key trends,
					challenges facing the industry, and potential opportunities that
					could be leveraged during the meeting for strategic advantage."""),
			verbose=True,
			llm= self.OpenAIGPT4
		)
	def solution_architect_agent(self):
		return Agent(
			role='Solution Architect',
			goal='Analyze the business problem and research and present a solution addressing the problem.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a GCP Solution Architect, your analysis will identify steps to solve business problem for client and come up with solution architecture."""),
			verbose=True,
			llm= self.OpenAIGPT4
		)
