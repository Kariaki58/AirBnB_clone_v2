#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity


storage_type = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """amenity class"""
    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
