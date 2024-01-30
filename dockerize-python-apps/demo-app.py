from flask import Flask

app = Flask(__name__)

# Route for the root path
@app.route('/')
def root():
    return '<html><body><h1>Hello. This is a article on Deploying docker container on ECS .!</h1></body></html>'

# Route for /health path
@app.route('/health')
def health():
    return 'Health OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
