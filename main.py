from db import init_db
from scraper import scrape_bbc_news
from api import app

if __name__ == "__main__":

   # Initialize database
   init_db()

   # Scrape BBC News homepage articles
   scrape_bbc_news()

   # Run Flask API
   app.run(host="127.0.0.1", port=5000, debug=True)