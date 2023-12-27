#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


storage_type = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """get list of city session from the db"""
            from models import storage
            from models.city import City
            list_data = []
            get_all_cities = storage.all(City)
            for key, value in get_all_cities.items():
                if value.state_id == self.id:
                    list_data.append(value)
            return list_data
