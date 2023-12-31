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
    file_content = file.read()
    print("File content: ", file_content)

    lines = file_content.split("\n")
    print("Lines: ", lines)

    for line in lines:
        topic = line.split(", ")
        print("Topic: ", topic)
        user_preferences.append(topic)

print("User preferences: ", user_preferences)

for user_preference in user_preferences:
    print("User preference: ", user_preference)

# Insert the users' preferences into the database
try:
    # Create a database connection
    connection = mysql.connector.connect(**DB_CONFIG)

    # Create a cursor object
    cursor = connection.cursor()

    # Insert the users' preferences into the database
    for user_id, user_preference in enumerate(user_preferences):
        for single_preference in user_preference:
            print(f'User ID: {user_id + 1}, Preference: {single_preference}')

            insert_user_preferences_query = """
            INSERT INTO user_preferences (user_id, topic)
            VALUES (%s, %s);
            """

            # Execute the SQL statements to insert the user preferences
            cursor.execute(insert_user_preferences_query, (user_id + 1, single_preference))

except Exception as e:
    print("Error occurred while inserting the user preferences: ", e)

# Commit changes, close the cursor and the connection
connection.commit()
cursor.close()
connection.close()
