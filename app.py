from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

FINNHUB_API_KEY ='d9oadhpr01qt6o9avri0d9oadhpr01qt6o9avrig'

@app.route('/')
def home():
    return jsonify({'message': 'Stock Tracker Running!'})
@app.route('/test')
def test():
    return "Test Working"

@app.route('/api/stock/<symbol>')
def get_stock(symbol):
    return jsonify({
        "symbol":symbol,
        "message":"Route is working"
    })
if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port=10000)
