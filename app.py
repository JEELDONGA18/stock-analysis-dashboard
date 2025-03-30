from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
from collections import deque

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Replace this with your Twelve Data API Key
API_KEY = "e047e2c6b3104488a41cc3cb41f7fcd1"

# Rate limiting setup
request_times = deque(maxlen=8)  # Store timestamps of the last 8 requests

# Function to check rate limit
def can_make_request():
    current_time = time.time()
    if len(request_times) < 8:
        request_times.append(current_time)
        return True
    elif current_time - request_times[0] > 60:
        request_times.popleft()
        request_times.append(current_time)
        return True
    return False

@app.route("/")
def home():
    return "Flask Server is Running!"

@app.route("/stock-data", methods=["GET"])
def get_stock_data():
    user_input = request.args.get("symbol", "").upper()
    duration = request.args.get("duration", "")

    if not user_input or not duration:
        return jsonify({"error": "Invalid company name or ticker code or duration"}), 400

    if not can_make_request():
        return jsonify({"error": "Rate limit exceeded. Please wait a minute."}), 429

    try:
        # API URL for Twelve Data
        url = f"https://api.twelvedata.com/time_series?symbol={user_input}&interval={duration}&apikey={API_KEY}"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch stock data"}), 500

        data = response.json()

        # Check if "values" exists and is a list
        if "values" not in data or not isinstance(data["values"], list):
            return jsonify({"error": data.get("message", "Unknown error occurred")}), 500

        # Return only the "values" array
        return jsonify(data["values"])
    except Exception as e:
        app.logger.error(f"Error fetching data: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
