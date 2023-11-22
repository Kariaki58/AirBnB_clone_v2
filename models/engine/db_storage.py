#!/usr/bin/python3
"""import modules"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """dbstorage"""
    __engine = None
    __session = None
    def __init__(self) -> None:
        """init session"""   
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
    
    def all(self, cls=None):
        if cls:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            data = self.__session.query(cls)
        else:
            classes = [User, State, City, Amenity, Place, Review]
            data = []
            for itter in classes:
                data.extend(self.__session.query(itter).all())
        obj_datas = {}
        for data in 
    
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        from models.user import User
        from models.city import Ctiy, Base
        from models.place import Place
        from models.state import State, Base
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
