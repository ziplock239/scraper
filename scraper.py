import requests
from bs4 import BeautifulSoup
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_movies():
    """
    Scrapes the latest movies from FZMovies.
    Returns a list of dictionaries containing title, link, and img.
    """
    url = "https://fzmovies.net/latest_movies.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://fzmovies.net/"
    }

    try:
        # Using a timeout to prevent hanging
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        movies = []

        # Target the movie listing items
        # FZMovies structure typically uses main_table_column for grid items
        items = soup.find_all('td', class_='main_table_column')
        
        if not items:
            logger.warning("No movie items found. The site structure might have changed.")
            return []

        for item in items:
            try:
                link_tag = item.find('a')
                img_tag = item.find('img')

                if link_tag and img_tag:
                    title = link_tag.get_text(strip=True)
                    relative_link = link_tag.get('href', '')
                    relative_img = img_tag.get('src', '')

                    # Clean up the title (sometimes contains extra whitespace)
                    clean_title = " ".join(title.split())
                    
                    # Construct absolute URLs
                    base_url = "https://fzmovies.net/"
                    full_link = relative_link if relative_link.startswith('http') else f"{base_url}{relative_link}"
                    full_img = relative_img if relative_img.startswith('http') else f"{base_url}{relative_img}"

                    movies.append({
                        "title": clean_title,
                        "link": full_link,
                        "img": full_img
                    })
            except Exception as item_error:
                logger.error(f"Error parsing specific movie item: {item_error}")
                continue
        
        logger.info(f"Successfully scraped {len(movies)} movies.")
        return movies

    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while scraping: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected scraping error: {e}")
        return []

if __name__ == "__main__":
    # Test block
    print("Testing scraper...")
    results = get_movies()
    for m in results[:5]:
        print(f"Found: {m['title']}")
