import os
from dotenv import load_dotenv
from scripts.scraper import get_all_books 
from scripts.processor import process_books
from scripts.reporter import df_to_csv
import logging
import logs.logger


logger = logging.getLogger(__name__)  
load_dotenv()


# orchestrates the entire pipeline
def run_pipeline():
    logger.info("Starting pipeline...")


    # Get the URL from environment variables
    url = os.environ.get("URL")
    if not url:
        logger.error("No URL found in environment variables")
        exit(1)

    
    try:
        # scrapes the website and gets books
        raw_books = get_all_books(url)

        # processes the raw books data into a DataFrame
        df = process_books(raw_books)

        # saves data into csv file
        df_to_csv(df)

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    run_pipeline()
