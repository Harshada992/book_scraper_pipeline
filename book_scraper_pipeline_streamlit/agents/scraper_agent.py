from crewai import Agent

scraper_agent = Agent(
    name="ScraperAgent",
    role="Web Scraper",
    goal="Extract book data from a public website",
    backstory="Expert in scraping structured HTML pages."
)
