import requests
from bs4 import BeautifulSoup
import mysql.connector
from config import DB_CONFIG


# This function will scrape and store news articles from the Google News
def scrape_and_store_google_news():
    # Google News URL
    google_news_url = "https://news.google.com"

    try:
        # Create a database connection
        connection = mysql.connector.connect(**DB_CONFIG)

        # Create a cursor - a middleware between the database and the application
        cursor = connection.cursor()

        # Send a HTTP GET request to the Google News URL
        response = requests.get(google_news_url)
        print("The HTTP GET request status is: ", response.status_code)

        # Check if the request was successful
        if(response.code == '200'):

            # Parse the response using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            articles =  soup.find_all("article")


    except Exception as e:
        print("Error occurred while scraping: ", e)


# This function will scrape and store news articles from the specified URL
def scrape_and_store_news():
    # Create a database connection
    connection = mysql.connector.connect(**DB_CONFIG)

    # Create a cursor - a middleware between the database and the application
    cursor = connection.cursor()

    # Retrieve the source name and URL from the database
    cursor.execute("SELECT source_name, source_url FROM scrape_sources_urls")
    sources = cursor.fetchall()

    for source_name, source_url in sources:
        try:
            # Send a HTTP GET request to the URL
            response = requests.get(source_url)
            print("The HTTP GET request status is: ", response.status_code)

            # Check if the request was successful
            if response.status == "200":
                # Parse the response using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract article information (customize as needed)
                title = soup.find("h1", class_="article-title").text
                author = soup.find("span", class_="author-name").text
                date_published = soup.find("span", class_="date").text
                content = soup.find("div", class_="article-body").text
                source = source_url

                # Insert the article into the database
                cursor.execute(
                    "INSERT INTO news_articles (title, author, date_published, content, source) VALUES (%s, %s, %s, %s, %s)",
                    (title, author, date_published, content, source),
                )

                # Commit the changes to the database
                connection.commit()

                # Print the article information
                print(f"Error scraping and storing data from {source_name}: {str(e)}")

        except Exception as e:
            print("Error occurred while scraping: ", e)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()


if __name__ == "__main__":
    scrape_and_store_google_news()
    print("Scraping completed successfully.")
