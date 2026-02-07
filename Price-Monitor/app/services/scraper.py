ib.parse import urljoin


def main():
    # scrapes all books into a list of dicts
    books = get_all_books(URL)
    
    print(f"scraped {len(books)} books")
    print(books[0])
    
    
def get_all_books(URL):
    books = []
    session, soup = scrape(URL)
    
    if not soup:
        raise RuntimeError("Failed to fetch initial page")

    while True:
        # Find all product blocks
        books_data = soup.find_all("article", class_="product_pod")
        for tag in books_data:
            book = {}
            book["title"] = tag.h3.a["title"]
            book["price_raw"] = tag.find("p", class_="price_color").text
            book["url"] = urljoin(URL, tag.h3.a["href"])
            
            books.append(book)
            
        # Try to find the "next" button
        next_button = soup.find("li", class_="next")
        if next_button:
            next_page_url = urljoin(URL, next_button.a["href"])
            URL = next_page_url  # update URL for urljoin to keep working

            response = session.get(next_page_url)
            soup = BeautifulSoup(response.text, "lxml")
        else:
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
        # Try to fetch the page
        response = session.get(url, timeout=10)   # timeout avoids hanging forever
        response.raise_for_status()               # raises error if status != 200

        # Try to parse the page
        soup = BeautifulSoup(response.text, "lxml")
        return session, soup

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None, None

    except Exception as e:
        print(f"Parsing error: {e}")
        return None, None



if __name__ == "__main__":
    main()