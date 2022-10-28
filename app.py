from flask import Flask
app = Flask(__name__)


@app.route('/')
def my_app():
    return '<h1>Hello, World!</h1>'
