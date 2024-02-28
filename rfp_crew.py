from rfp_agents import RFPAgents
from rfp_tasks import RFPTasks
from textwrap import dedent
from crewai import Crew
import streamlit as st


class RFPCrew():

    def __init__(self, company, competitors, business_problem, industry):
        self.company = company
        self.competitors = competitors
        self.business_problem = business_problem
        self.industry = industry

    def run(self):
        agents = RFPAgents()
        tasks = RFPTasks()
        industry_analysis_agent = agents.industry_analysis_agent()
        solution_architect_agent = agents.solution_architect_agent()
        industry_analysis_task = tasks.industry_analysis_task(
        industry_analysis_agent,
        self.company,
        self.competitors,
        self.business_problem,
        self.industry
        )
        solution_architect_task = tasks.solution_architecture_task(
        solution_architect_agent,
        self.company,
        self.competitors,
        self.business_problem,
        self.industry
        )
        crew = Crew(
        agents=[industry_analysis_agent, solution_architect_agent],
        tasks=[industry_analysis_task, solution_architect_task],
        verbose=True,
        full_output= True,
        share_crew=False
        )
        output = crew.kickoff()
        st.info(output)
        return output