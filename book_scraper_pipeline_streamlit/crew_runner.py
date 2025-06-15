from crewai import Agent, Task, Crew
from agents.scraper_agent import scraper_agent
from agents.etl_agent import etl_agent
from scraper.scrape_site import smart_scrape
from etl.load import transform_and_save

# Take input from user
url = input("Enter the website URL to scrape: ").strip()

scrape_task = Task(
    agent=scraper_agent,
    description=f"Scrape structured content from {url}",
    expected_output="Structured data from the provided webpage"
)

etl_task = Task(
    agent=etl_agent,
    description="Transform and save the scraped data to a CSV",
    expected_output="A cleaned CSV file with the scraped data"
)

# Execute actual pipeline logic
data = smart_scrape(url)
transform_and_save(data, url)

# CrewAI agents overview
crew = Crew(
    agents=[scraper_agent, etl_agent],
    tasks=[scrape_task, etl_task]
)

crew.run()
