from pathlib import Path
import logging

logger = logging.getLogger(__name__)   


def df_to_csv(df, filename="books.csv", folder="data"):
    """
    Save a DataFrame to CSV in a given folder.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): Name of the CSV file (default: 'books.csv').
        folder (str): Directory to save the file (default: 'data').
    """
    try:
        # Ensure folder exists
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured folder exists: {path.resolve()}")

        # Build full file path
        file_path = path / filename
        logger.debug(f"Saving DataFrame to {file_path.resolve()}")

        # Save DataFrame
        df.to_csv(file_path, index=False, encoding="utf-8")

        logger.info(f"DataFrame successfully saved to {file_path.resolve()}")

    except Exception as e:
        logger.exception("Failed to save DataFrame")
        raise RuntimeError(f"Failed to save DataFrame: {e}")
