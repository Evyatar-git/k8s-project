"""
This module contains the Flask application for the frontend service.
"""

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Backend API URL
import os
BACKEND_API_URL = os.environ.get("BACKEND_URL", "http://backend:5001")


@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template("index.html")

@app.route('/fetch_price', methods=['GET'])
def fetch_price():
    response = requests.get(f"{BACKEND_API_URL}/fetch_price")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to fetch prices from backend"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
