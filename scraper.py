import requests
from bs4 import BeautifulSoup
import mysql.connector
from config import DB_CONFIG


# This function will scrape and store news articles from the Google News
def scrape_and_store_google_news(user_id):
    # Google News URL
    google_news_url = "https://news.google.com"

    try:
        # Create a database connection
        connection = mysql.connector.connect(**DB_CONFIG)

        # Create a cursor - a middleware between the database and the application
        cursor = connection.cursor()

        # Fetch the user's preferences from the database by user_id
        cursor.execute("SELECT topic, language FROM user_preferences WHERE user_id = %s", (user_id,))
        user_preferences = cursor.fetchall()

        for topic, language in user_preferences:
            # Customize the Google News URL based on the user's preferences
            google_news_topic_url = f"{google_news_url}/topics/{topic}?hl={language}"

            # Send a HTTP GET request to the Google News URL
            response = requests.get(google_news_topic_url)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the response using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")

        # Send a HTTP GET request to the Google News URL
        response = requests.get(google_news_url)
        print("The HTTP GET request status is: ", response.status_code)

        # Check if the request was successful
        if response.code == 200:
            # Parse the response using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all the news articles on the Google News front page
            articles = soup.find_all("article")

            for article in articles:
                # Extract the article information (customize as needed)
                title = article.find("h3").text
                author = article.find("a", class_="wEwyrc ").text
                date_published = article.find("time")["datetime"]
                source = article.find("a", class_="VDXfz").get("href")

                # Insert the article into the database
                cursor.execute(
                    "INSERT INTO news_articles (title, author, date_published, source) VALUES (%s, %s, %s, %s)",
                    (title, author, date_published, source),
                )

                # Commit the changes to the database
                connection.commit()

                # Print the article information
                print(
                    "Article title: ",
                    title,
                    "\nArticle author: ",
                    author,
                    "\nDate published: ",
                    date_published,
                    "\nSource: ",
                    source,
                )

    except Exception as e:
        print("Error occurred while scraping: ", e)

    finally:
        # Close the cursor
        cursor.close()

        # Close the connection
        connection.close()


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
            if response.status == 200:
                # Parse the response using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")

                # Extract article information (customize as needed)
                title = soup.find("h1", class_="article-title").text
                author = soup.find("span", class_="author-name").text
                date_published = soup.find("span", class_="date").text
                source = source_url

                # Insert the article into the database
                cursor.execute(
                    "INSERT INTO news_articles (title, author, date_published, source) VALUES (%s, %s, %s, %s)",
                    (title, author, date_published, source),
                )

                # Commit the changes to the database
                connection.commit()

                # Print the article information
                print(
                    "Article title: ",
                    title,
                    "\nArticle author: ",
                    author,
                    "\nDate published: ",
                    date_published,
                    "\nSource: ",
                    source,
                )

        except Exception as e:
            print("Error occurred while scraping: ", e)

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()


if __name__ == "__main__":
    scrape_and_store_google_news()
    print("Scraping completed successfully.")
