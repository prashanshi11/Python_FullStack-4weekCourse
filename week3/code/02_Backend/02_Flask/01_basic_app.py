# 01_basic_app.py
# A minimal Flask application with a single route

from flask import Flask

app = Flask(__name__)  # Create Flask app instance

@app.route('/')  # Define route for homepage
def home():
    return '<h1>Hello, Flask!</h1><p>Welcome to your first Flask app.</p>'

if __name__ == '__main__':
    app.run(debug=True)
