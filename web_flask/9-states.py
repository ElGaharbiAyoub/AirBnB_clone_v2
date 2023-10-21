#!/usr/bin/python3
""" doc flask"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    states = storage.all('State')
    return render_template('9-states.html', states=states, state=None)


@app.route('/states/<id>', strict_slashes=False)
def cities_states_list(id):
    state = storage.all('State').get('State.{}'.format(id))
    return render_template('9-states.html', state=state, states=None)


@app.teardown_appcontext
def closer(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
