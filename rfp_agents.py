import os
from textwrap import dedent
from crewai import Agent
from tools.ExaSearchTool import ExaSearchTool
from rfp_model import ChatModel
from dotenv import load_dotenv

class RFPAgents:
	def __init__(self):
		load_dotenv()
		self.llm = ChatModel().localMistral

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
			max_iter=3,
			llm= self.llm
		)
	def solution_architect_agent(self):
		return Agent(
			role='Solution Architect',
			goal='Analyze the business problem and research and present a solution addressing the problem.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					As a GCP Solution Architect, your analysis will identify steps to solve business problem for client and come up with solution architecture."""),
			verbose=True,
			max_iter=3,
			llm= self.llm
		)
