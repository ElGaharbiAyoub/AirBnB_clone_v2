#!/usr/bin/python3
""" doc flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/",  strict_slashes=False)
def hello():
    """start flask"""
    return "Hello HBNB!"


@app.route("/hbnb",  strict_slashes=False)
def hbnb():
    """start flask"""
    return "HBNB"


@app.route("/c/<text>",  strict_slashes=False)
def printC(text):
    """display slag"""
    slag = text.replace("_", " ")
    return "C {}".format(slag)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>",  strict_slashes=False)
def printPython(text):
    """display slag"""
    slag = text.replace("_", " ")
    return "C {}".format(slag)


@app.route("/number/<int:n>",  strict_slashes=False)
def printNumber(n):
    """display slag number"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
