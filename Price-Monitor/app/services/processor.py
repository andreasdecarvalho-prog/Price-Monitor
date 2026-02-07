from app.core.config import BASE_URL as URL
from app.services.scraper import get_all_books
import pandas as pd


def main():
    # Scrape raw book data from the website
    raw_books = get_all_books(URL)

    # Process raw data into a clean DataFrame
    df = process_books(raw_books)

    # Print quick checks on the processed data
    print(df.head())        # preview first 5 rows
    print(df.dtypes)        # check column data types
    print(df.isna().sum())  # count missing values per column


def process_books(raw_books):
    """
    Convert a list of raw book dictionaries into a cleaned pandas DataFrame.
    Ensures required columns exist, parses prices into floats, and removes duplicates.
    """
    try:
        # Validate input
        if not raw_books:
            raise ValueError("No raw books received from scraper")

        # Convert list of dicts into DataFrame
        df = pd.DataFrame(raw_books)

        # Ensure required columns are present
        required_cols = {"title", "price_raw", "url"}
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        # Parse "price_raw" strings into numeric floats
        # Example: "£51.77" → 51.77
        df["price"] = (
            df["price_raw"]
            .str.replace("£", "", regex=False)   # remove pound symbol
            .str.replace("Â", "", regex=False)   # remove stray encoding artifact
            .astype(float)                       # convert to float
        )
        df.drop(columns=["price_raw"], inplace=True)

        # Remove duplicate books by title, keeping the first occurrence
        df.drop_duplicates(subset="title", keep="first", inplace=True)
        
        return df

    except Exception as e:
        # Wrap any error into a RuntimeError for clarity
        raise RuntimeError(f"Processing failed: {e}")


if __name__ == "__main__":
    # Run the pipeline stage when executed directly
    main()