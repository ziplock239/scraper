# MovieStream Scraper App

A production-ready Flask application that scrapes the latest movie uploads from FZMovies and displays them in a modern, responsive, Netflix-style UI using Tailwind CSS. Optimized for deployment on Render.

## Features
-   **Automated Scraping**: Uses `BeautifulSoup4` and `requests` to fetch the latest movie data.
-   **Modern UI**: Fully responsive grid layout with hover animations and mobile optimization.
-   **Deployment Ready**: Pre-configured with `Gunicorn`, `Procfile`, and `runtime.txt` for Render/Heroku.
-   **Robust Error Handling**: Handles network timeouts and missing image fallbacks gracefully.

## Prerequisites
-   Python 3.11 or higher
-   Pip (Python package manager)
-   Git (for deployment)

## Local Installation

1.  **Clone the files** (or download the zip) into a project folder.

2.  **Create a Virtual Environment**:
    python -m venv venv

3.  **Activate Virtual Environment**:
    -   Windows: `venv\Scripts\activate`
    -   macOS/Linux: `source venv/bin/activate`

4.  **Install Dependencies**:
    pip install -r requirements.txt

5.  **Run the Application**:
    python app.py

6.  **Access the App**:
    Open `http://127.0.0.1:5000` in your browser.

## Deployment to Render

1.  **Prepare Repository**:
    -   Initialize git: `git init`
    -   Add files: `git add .`
    -   Commit: `git commit -m "Initial commit"`
    -   Push to a GitHub repository.

2.  **Create Render Web Service**:
    -   Log in to [Render](https://render.com).
    -   Click **New** > **Web Service**.
    -   Connect your GitHub repository.

3.  **Configuration Settings**:
    -   **Runtime**: `Python 3`
    -   **Build Command**: `pip install -r requirements.txt`
    -   **Start Command**: `gunicorn app:app`

4.  **Environment Variables**:
    -   You can optionally add `SECRET_KEY` in the Render Dashboard, though the app has a default.

## Project Structure
-   `app.py`: The Flask server and route handling.
-   `scraper.py`: Logic for scraping fzmovies.net.
-   `templates/`: HTML templates (index.html).
-   `requirements.txt`: Python package dependencies.
-   `Procfile`: Process file for Gunicorn production server.
-   `runtime.txt`: Specifies the Python version for Render.

## Troubleshooting
-   **Empty Grid**: If no movies appear, FZMovies might be blocking the request from Render's IP addresses or their HTML structure has changed. Check the Render logs for "Scraping Error".
-   **Slow Loading**: The app scrapes on every refresh. For production usage, consider implementing a simple cache using `Flask-Caching`.
