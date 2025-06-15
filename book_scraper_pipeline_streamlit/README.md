# Book Scraper Pipeline with CrewAI

This project scrapes daily product data from [books.toscrape.com](http://books.toscrape.com), transforms it, and stores it in a CSV using CrewAI agents.

## Structure
- `scraper/`: Contains the scraping logic.
- `etl/`: Contains transformation and CSV saving logic.
- `agents/`: CrewAI agents for scraping and ETL.
- `crew_runner.py`: Runs the agents and tasks.
- `scheduler.py`: Schedules the run daily at 9AM.

## Run Once
```bash
python crew_runner.py
```

## Run Daily
```bash
python scheduler.py
```

## Install Requirements
```bash
pip install -r requirements.txt
```
