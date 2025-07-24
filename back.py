from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/getdata', methods=['GET'])
def get_data():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing URL parameter"}), 400

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#http://127.0.0.1:5000/api/getdata?url=https://www.hdfcbank.com/

if __name__ == '__main__':
    app.run(debug=True, port=5000)
