from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Get API key from Render Environment Variable
API_KEY = os.getenv("FINNHUB_API_KEY")


@app.route("/")
def home():
    return jsonify({
        "message": "Stock Tracker API is running"
    })


@app.route("/stock/<symbol>")
def get_stock(symbol):

    if not API_KEY:
        return jsonify({
            "error": "API key not found in server"
        }), 500

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol.upper()}&token={API_KEY}"

    try:
        response = requests.get(url)

        data = response.json()

        # Finnhub returns empty values if symbol is wrong
        if "c" not in data or data.get("c") == 0:
            return jsonify({
                "error": "Stock not found",
                "symbol": symbol
            }), 404

        return jsonify({
            "symbol": symbol.upper(),
            "current_price": data.get("c"),
            "change": data.get("d"),
            "percent_change": data.get("dp"),
            "high": data.get("h"),
            "low": data.get("l"),
            "open": data.get("o"),
            "previous_close": data.get("pc")
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


