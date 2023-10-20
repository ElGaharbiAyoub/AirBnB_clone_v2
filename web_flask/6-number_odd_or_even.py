#!/usr/bin/python3
""" doc flask"""
from flask import Flask, render_template

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
    return "Python {}".format(slag)


@app.route("/number/<int:n>",  strict_slashes=False)
def printNumber(n):
    """display slag number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display slag number"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display slag number"""
    if isinstance(n, int):
        is_even = n % 2 == 0
        return render_template(
            '6-number_odd_or_even.html', number=n, is_even=is_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
