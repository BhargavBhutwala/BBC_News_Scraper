import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from db import insert_article

def scrape_bbc_news():

   """Scrape BBC News homepage articles."""

   options = Options()
   options.headless = True
   options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

   driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=options
   )

   baseUrl = "https://www.bbc.com"
   driver.get(baseUrl)
   time.sleep(2)

   articles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="dundee-card"]')
   print(f"Found {len(articles)} articles")

   for article in articles:

      try:

         # Extracting URL from <a> tag
         link_elems = article.find_elements(By.CSS_SELECTOR, 'a[data-testid="internal-link"]')
         if not link_elems:
            # If not found, try the external link
            link_elems = article.find_elements(By.CSS_SELECTOR, 'a[data-testid="external-anchor"]')
         if link_elems:
            url = link_elems[0].get_attribute('href')
         else:
            print("No link found for this article, skipping it.")
            continue

         # Extracting title from <h2> tag
         title_elem = article.find_element(By.CSS_SELECTOR, 'h2[data-testid="card-headline"]')
         title = title_elem.text.strip()

         # Extracting summary from <p> tag
         try:
            summary_elem = article.find_element(By.CSS_SELECTOR, 'p[data-testid="card-description"]')
            summary = summary_elem.text.strip()
         except Exception:
            summary = "Summary not available"

         # Extracting publication date from <span> tag
         try:
            time_elem = article.find_element(By.CSS_SELECTOR, 'span[data-testid="card-metadata-lastupdated"]')
            publication_date = time_elem.text.strip()
         except Exception:
            publication_date = "Publication date not available"

         # Extracting category from <span> tag
         try:
            category_elem = article.find_element(By.CSS_SELECTOR, 'span[data-testid="card-metadata-tag"]')
            category = category_elem.text.strip()
         except Exception:
            category = "Category not available"

         article_data = {
            'title': title,
            'summary': summary,
            'url': url,
            'publication_date': publication_date,
            'category': category
         }
         print("Scraped: ", article_data)

         # Insert article into the database
         insert_article(article_data)

      except Exception as e:
         print("Error scraping an article: ", e)
         traceback.print_exc()

   driver.quit()

