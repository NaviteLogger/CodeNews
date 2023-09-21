import requests
from bs4 import BeautifulSoup
import mysql.connector
from config import DB_CONFIG

# This function will scrape and store news articles from the specified URL
def scrape_and_store_news():
    # Create a database connection
    connection = mysql.connector.connect(**DB_CONFIG)

    # Create a cursor - a middleware between the database and the application
    cursor = connection.cursor()

    #Retrieve the source name and URL from the database
    cursor.execute("SELECT source_name, source_url FROM scrape_sources_urls")
    sources = cursor.fetchall()