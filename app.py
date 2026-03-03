from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    if request.method == 'POST':
        url = request.form['url']
        # Forward the request to the target URL
        try:
            response = requests.get(url)
            return response.content, response.status_code, response.headers.items()
        except requests.exceptions.RequestException as e:
            return str(e), 500
    return 'Only POST requests are allowed.', 405

if __name__ == '__main__':
    app.run(debug=True)