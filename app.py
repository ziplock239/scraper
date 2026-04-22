import os
from flask import Flask, render_template, jsonify
from scraper import get_movies

app = Flask(__name__)

# Security configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-12345')

@app.route('/')
def index():
    """
    Renders the main dashboard with scraped movie data.
    """
    try:
        movies_list = get_movies()
        return render_template('index.html', movies=movies_list)
    except Exception as e:
        app.logger.error(f"Template rendering error: {e}")
        return "An internal error occurred while loading movies.", 500

@app.route('/api/movies')
def api_movies():
    """
    Endpoint for fetching movie data as JSON.
    Useful for frontend refreshes or mobile app integration.
    """
    movies_list = get_movies()
    return jsonify(movies_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', movies=[], error="Page not found"), 404

if __name__ == '__main__':
    # Configuration for local development
    # Render will use the Gunicorn command in the Procfile
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
