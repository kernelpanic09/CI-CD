from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, CI/CD!')

@app.route('/health')
def health():
    return jsonify(status='UP')

@app.route('/status')
def status():
    return jsonify(service='Example CI/CD Pipeline', status='Running', version='1.0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
