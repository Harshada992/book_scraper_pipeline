import pandas as pd
from datetime import datetime
from loguru import logger
import re

def sanitize_filename(url):
    return re.sub(r'\W+', '_', url)

def transform_and_save(data, url):
    logger.add("pipeline.log", rotation="1 MB")
    try:
        df = pd.DataFrame(data)
        filename = f"scraped_{sanitize_filename(url)}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        df.to_csv(filename, index=False)
        logger.success(f"Data saved to {filename}")
    except Exception as e:
        logger.error(f"Failed to transform and save: {e}")
