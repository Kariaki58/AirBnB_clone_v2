#!/usr/bin/python3
"""list of states"""
from models import storage
from flask import Flask, render_template
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(session):
    """close session after each request"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb_clone():
    """ Route function for /states and /states/<id> """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    sorted_states = sorted(states.values(), key=lambda item: item.name)
    sorted_amenit = sorted(amenities.values(), key=lambda x: x.name)
    return render_template(
        '100-hbnb.html', states=sorted_states, amenities=sorted_amenit
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
