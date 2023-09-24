# Make sure that before you run this script, the .env file db user can create tables in your database

import mysql.connector
from config import DB_CONFIG

# Create a database connection
connection = mysql.connector.connect(**DB_CONFIG)

# Create a cursor object
cursor = connection.cursor()

try:
    # Create the 'news_articles' table
    create_news_articles_table_query = """
    CREATE TABLE IF NOT EXISTS news_articles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT,
        source VARCHAR(255) NOT NULL,
        date_published DATE
    );
    """

    # Execute the SQL statements to create the table
    cursor.execute(create_news_articles_table_query)

    # Create the 'scrape_sources_urls' table
    create_scrape_sources_urls_table_query = """
    CREATE TABLE IF NOT EXISTS scrape_sources_urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source_name VARCHAR(255) NOT NULL,
    source_url VARCHAR(255) NOT NULL
    );
    """

    # Execute the SQL statements to create the table
    cursor.execute(create_scrape_sources_urls_table_query)

    # Create the 'user_preferences' table
    create_user_preferences_table_query = """
    CREATE TABLE IF NOT EXISTS user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    topic VARCHAR(255) NOT NULL,
    language VARCHAR(255) NOT NULL
    );
    """

    # Execute the SQL statements to create the table
    cursor.execute(create_user_preferences_table_query)

except Exception as e:
    print("Error occurred while initializing the database schema: ", e)

finally:
    # Commit the changes to the database
    connection.commit()
    
    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()

    print("Database schema initialized successfully.")

# Read the users' preferences from the text file into an array
user_preferences = []

with open("user_preferences.txt", "r") as file:
    for line in file:
        topic = line.strip.split(", ")
        user_preferences.append(topic)

# Insert the users' preferences into the database
try:
    # Create a database connection
    connection = mysql.connector.connect(**DB_CONFIG)

    # Create a cursor object
    cursor = connection.cursor()

    for preferences in user_preferences:
        # Extract topics from the users' preferences
        topic = preferences[0]

        # Insert topics into the user_preferences table
        insert_user_preferences_query = """
        INSERT INTO user_preferences (topic) VALUES (%s)
        """

        cursor.execute(insert_user_preferences_query, (topic))

except Exception as e:
    print("Error occurred while inserting the user preferences: ", e)

# Commit changes, close the cursor and the connection
connection.commit()
cursor.close()
connection.close()
