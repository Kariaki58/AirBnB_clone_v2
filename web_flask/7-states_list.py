#!/usr/bin/python3
"""list of states"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)

states = storage.all(State)


@app.teardown_appcontext
def remove_session(session):
    """close session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """state router"""
    dictionary = {}
    listofdictionary = []
    for data in states.values():
        dictionary['name'] = data.name
        dictionary['id'] = data.id
        listofdictionary.append(dictionary)
    sorted_data = sorted(listofdictionary, key=lambda x: x['name'])
    return render_template('7-states_list.html', sorted_data=sorted_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
