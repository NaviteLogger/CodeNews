import mysql.connector
from config import DB_CONFIG

# Create a database connection
connection = mysql.connector.connect(**DB_CONFIG)

# Create a cursor object
cursor = connection.cursor()

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

# Commit changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Database schema initialized successfully.")
