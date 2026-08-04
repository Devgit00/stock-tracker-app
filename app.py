from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

FINNHUB_API_KEY ='d9oadhpe01qt6o9avrig'

@app.route('/')
def home():
    return jsonify({'message': 'Stock Tracker Running!'})
@app.route('/test')
def test():
    return "Test Working"

@app.route('/api/stock/<symbol>')
def get_stock(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        data = requests.get(url, timeout=10).json()
        return jsonify({
            'symbol': symbol,
            'price': data.get('c'),
            'change': data.get('d'),
            'changePercent': data.get('dp')
        })
    except:
        return jsonify({'error': 'API Error'}), 500

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port=10000)
