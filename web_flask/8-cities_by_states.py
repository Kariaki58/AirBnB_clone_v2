#!/usr/bin/python3
"""list of states"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(session):
    """close session after each request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """state router"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda item: item.name)
    return render_template('8-cities_by_states.html', sorted_states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
