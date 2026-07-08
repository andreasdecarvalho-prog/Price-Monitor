from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)   

def get_all_books(URL):
    logger.info(f"Scraping started at {URL}")
    books = []
    session, soup = scrape(URL)
    
    if not soup:
        logger.error("Failed to fetch initial page")
        raise RuntimeError("Failed to fetch initial page")

    page_count = 1
    while True:
        logger.debug(f"Scraping page {page_count} from {URL}")

        # Find all product blocks
        books_data = soup.find_all("article", class_="product_pod")
        logger.debug(f"Found {len(books_data)} books on page {page_count}")

        for tag in books_data:
            book = {
                "title": tag.h3.a["title"],
                "price_raw": tag.find("p", class_="price_color").text,
                "url": urljoin(URL, tag.h3.a["href"]),
            }
            books.append(book)

        # Try to find the "next" button
        next_button = soup.find("li", class_="next")
        if next_button:
            next_page_url = urljoin(URL, next_button.a["href"])
            URL = next_page_url  # update URL for urljoin to keep working

            logger.debug(f"Moving to next page: {next_page_url}")
            response = session.get(next_page_url)
            soup = BeautifulSoup(response.text, "lxml")
            page_count += 1
        else:
            logger.info(f"Finished scraping. Total books collected: {len(books)}")
            return books  # no more pages, stop the loop


def scrape(url):
    # Create session
    session = requests.Session()

    # Add headers
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }
    )

    try:
        logger.debug(f"Fetching URL: {url}")
        response = session.get(url, timeout=10)   # timeout avoids hanging forever
        response.raise_for_status()               # raises error if status != 200

        logger.debug(f"Response status: {response.status_code}")
        soup = BeautifulSoup(response.text, "lxml")
        logger.debug("Successfully parsed HTML")
        return session, soup

    except requests.exceptions.RequestException as e:
        logger.exception(f"Request failed for {url}")
        raise RuntimeError(e)

    except Exception as e:
        logger.exception("Unexpected error during scraping")
        raise RuntimeError(e)
