import mysql.connector
from config import DB_CONFIG

# Create a database connection
connection = mysql.connector.connect(**DB_CONFIG)

# Create a cursor object
cursor = connection.cursor()

# Define SQL statements to create tables (customize these based on your project needs)
create_table_query = """
CREATE TABLE IF NOT EXISTS news_articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    source VARCHAR(255),
    date_published DATE
);
"""

# Execute the SQL statements
cursor.execute(create_table_query)

# Commit changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Database schema initialized successfully.")
