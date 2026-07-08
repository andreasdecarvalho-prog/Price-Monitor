import pandas as pd
import logging

logger = logging.getLogger(__name__)   
def process_books(raw_books):
    """
    Convert a list of raw book dictionaries into a cleaned pandas DataFrame.
    Ensures required columns exist, parses prices into floats, and removes duplicates.
    """
    try:
        # Validate input
        if not raw_books:
            logger.error("No raw books received from scraper")
            raise ValueError("No raw books received from scraper")

        logger.info(f"Processing {len(raw_books)} raw book records")

        # Convert list of dicts into DataFrame
        df = pd.DataFrame(raw_books)
        logger.debug(f"Initial DataFrame shape: {df.shape}")

        # Ensure required columns are present
        required_cols = {"title", "price_raw", "url"}
        missing = required_cols - set(df.columns)
        if missing:
            logger.error(f"Missing columns: {missing}")
            raise ValueError(f"Missing columns: {missing}")

        # Parse "price_raw" strings into numeric floats
        logger.debug("Parsing price_raw into numeric values")
        df["price"] = (
            df["price_raw"]
            .str.replace("£", "", regex=False)   # remove pound symbol
            .str.replace("Â", "", regex=False)   # remove stray encoding artifact
            .astype(float)                       # convert to float
        )
        df.drop(columns=["price_raw"], inplace=True)

        # Remove duplicate books by title, keeping the first occurrence
        before_dedup = df.shape[0]
        df.drop_duplicates(subset="title", keep="first", inplace=True)
        after_dedup = df.shape[0]
        logger.debug(f"Removed {before_dedup - after_dedup} duplicate titles")

        logger.info(f"Final DataFrame shape: {df.shape}")
        return df

    except Exception as e:
        logger.exception("Processing failed")
        raise RuntimeError(f"Processing failed: {e}")
