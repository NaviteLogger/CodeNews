# CodeNews: AI-Powered Programming Language News Aggregator

CodeNews is a Python-based project that provides a convenient way to stay up to date with the latest news, updates, and changes related to programming languages and technologies. It utilizes web scraping, natural language processing (NLP), and personalized recommendations to deliver curated news articles based on your interests.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Database Setup](#database-setup)
- [Usage](#usage)
  - [Running the Web Scraper](#running-the-web-scraper)
  - [Summarizing News Articles](#summarizing-news-articles)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these steps to set up and run CodeNews on your local machine.

### Prerequisites

- Python 3.x
- MySQL (or another database of your choice)

### Setting Up a Virtual Environment

1. Clone this repository:

   ```bash
   git clone https://github.com/NaviteLogger/CodeNews.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CodeNews
   ```

3. Create a virtual environment (optional):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

### Install Dependencies

1. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Configure your MySQL database settings in `config.py`. Update the following fields with your database information:

```python
DB_CONFIG = {
    "host": "your_database_host",
    "user": "your_database_user",
    "password": "your_database_password",
    "database": "your_database_name",
}
```

2. Initialize the database schema by running the following command:

```bash
python init_db.py
```

## Usage

### Running the Web Scrapper:

1. Start the web scraping component to collect news articles:

```bash
python scraper.py
```

This script will periodically scrape news articles from selected sources and store them in the MySQL database for further processing.

2. Access the summarized news articles through your preferred frontend or API, which you can develop based on the project's needs.

## Contributing

Contributions are welcome! Feel free to submit issues, suggest improvements, or make pull requests to help enhance this project.

## License


