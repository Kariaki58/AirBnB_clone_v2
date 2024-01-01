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

@app.route("/states", strict_slashes=False)
def states():
    states = storage.all(State)
    sortedd = sorted(states.values(), key=lambda item: item.name)
    return render_template("9-states.html", states=sortedd, check="none")


@app.route("/states/<id>")
def states_id(id):
    dictionary = {}
    states = storage.all(State)
    check = False
    for state in states.values():
        if id == state.id:
            check = True
            dictionary = state
    return render_template("9-states.html", states=dictionary, check=check)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
