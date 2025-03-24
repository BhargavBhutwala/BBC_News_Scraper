# BBC News Scraper & API

This project is a backend service that scrapes articles from the [BBC News website](https://www.bbc.com/news), stores the scraped data in a MySQL database, and provides a REST API to retrieve and manage the data. The project uses Python, Selenium, Flask, and MySQL. It is structured in a modular fashion with separate modules for scraping, database operations, and the API.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)

## Features

- **Web Scraper**: Uses Selenium (with headless Chrome) to scrape BBC News articles.
- **Database Storage**: Stores article data (title, summary, URL, publication date, category) in a MySQL database.
- **REST API**: Provides endpoints to:
  - Retrieve all articles with pagination.
  - Retrieve articles by category.
  - Delete an article by its ID.
- **CORS Enabled**: Allows cross-origin requests for front-end integration.
- **Modular Code**: Organized into separate modules for scraping, database operations, and API endpoints.

## Requirements

- Python 3.7+
- MySQL
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (managed automatically with `webdriver-manager`)

- `selenium`
- `flask`
- `flask-cors`
- `mysql-connector-python`
- `webdriver-manager`

## Usage

The scraper uses Selenium to scrape articles from BBC News. It extracts the title, summary, URL, publication date, and category. Some articles have either an internal or external link; both cases are handled.

To run the scraper and start the API:

1. Run the main script:

python main.py

Note:

The main.py file initializes the database, runs the scraper, and then starts the Flask API.

For testing the API without waiting for scraping, you can comment out the scrape_bbc_news() call in main.py.
