from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "You reached the Index page! Welcome to the Flask App!"

@app.route('/home')
def home():
    return "You reached the Home page! Don't search around🤨"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)