from crewai import Agent

etl_agent = Agent(
    name="ETLAgent",
    role="Data Cleaner",
    goal="Transform and save scraped book data to CSV",
    backstory="Specialist in formatting and saving data efficiently."
)
