from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

import os




@CrewBase
class Deepeek():
	"""Deepeek crew"""


	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	deepseek_ollama = LLM (
		model= "ollama/deepseek-r1:1.5b",
		base_url = "http://localhost:11434"
	)

	perplexity = LLM(
    model="perplexity/sonar-reasoning",
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
     )





	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			llm=self.perplexity
		)
	
	@agent
	def google_collector(self) -> Agent:
		return Agent(
			config=self.agents_config['google_collector'],
			verbose=True,
			#tools=[SerperDevTool()]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=self.perplexity
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			llm=self.perplexity
		)
	
	@task
	def google_task(self) -> Task:
		return Task(
			config=self.tasks_config['google_task']
		)



	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
			
		)



	@crew
	def crew(self) -> Crew:
		"""Creates the Deepeek crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
