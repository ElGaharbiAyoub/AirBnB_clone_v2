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
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
