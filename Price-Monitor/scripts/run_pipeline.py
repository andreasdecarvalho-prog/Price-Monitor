from app.core.config import BASE_URL as URL
from app.services.scraper import get_all_books 
from app.services.processor import process_books
from app.services.reporter import df_to_csv
from app.services.delivery import send_email
from app.services.delivery import update_sheet

def run_pipeline():
    raw_books = get_all_books(URL)
    df = process_books(raw_books)
    df_to_csv(df)
    send_email("data/books.csv")
    update_sheet(df)
    
    print("Pipeline executed")

    
    

if __name__ == "__main__":
    run_pipeline()
