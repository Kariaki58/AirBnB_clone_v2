#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

states = storage.all()
for data, value in states.items():
    print(value)