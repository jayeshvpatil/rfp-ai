from textwrap import dedent
from crewai import Task


class RFPTasks():
	def industry_analysis_task(self, agent, company, competitors, business_problem, industry):
		return Task(
			description=dedent(
				f"""\
				Analyze the current industry trends, challenges, and opportunities
				relevant to below company and it's business problem. Consider market reports, recent
				developments, and expert opinions to provide a comprehensive
				overview of the industry landscape.

				Company: {company}
				Business Problem: {business_problem}
				Competitors : {competitors}
                Industry : {industry}
                """),
			expected_output=dedent("""\
				A detailed report summarizing key findings about each company
				and it's competitors, highlighting information that could be relevant for the RFP's business problem."""),
			async_execution=True,
			agent=agent
		)
	def solution_architecture_task(self, agent, company, competitors, business_problem, industry):
		return Task(
			description=dedent(
				f"""\
				Analyze the business problem. Research and present a google cloud solution to address the problem. Discuss the solution architecture and components.
				Keep it concise and short.
				Company: {company}
				Business Problem: {business_problem}
				Competitors : {competitors}
				Industry : {industry}
				"""),
			expected_output=dedent("""\
				A detailed report summarizing key findings about the solution solving the business problem, highlighting information that could be relevant for the RFP's business problem."""),
			async_execution=True,
			agent=agent
		)
