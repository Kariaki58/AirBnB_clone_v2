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
