# src/app.py
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/health')
def health():
    """Return the health status."""
    return jsonify(status='UP')

@app.route('/status')
def status():
    """Return the service status."""
    return jsonify(service='Example CI/CD Pipeline', status='Running', version='1.0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
