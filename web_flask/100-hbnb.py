#!/usr/bin/python3
""" doc flask"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def cities_states_list():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html', amenities=amenities, states=states, places=places)


@app.teardown_appcontext
def closer(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
