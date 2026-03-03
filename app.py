from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TARGET_URL = 'http://example.com'

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    if request.method == 'GET':
        response = requests.get(TARGET_URL, params=request.args)
    else:
        response = requests.post(TARGET_URL, json=request.json)

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)