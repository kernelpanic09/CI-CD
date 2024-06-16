from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a welcome message."""
    return jsonify(message='Hello, CI/CD!')

@app.route('/health')
def health():
    """Return the health status."""
    return jsonify(status='UP')

@app.route('/status')
def status():
    """Return the service status."""
    return jsonify(service='Example CI/CD Pipeline', status='Running', version='1.0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
