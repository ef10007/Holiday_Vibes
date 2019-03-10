from holvflask.pro_init_db import Base
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref

class London(Base):
    __tablename__ = 'London'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    price = Column(Integer)

class Sydney(Base):
    __tablename__ = 'Sydney'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    price = Column(Integer)

class Newyork(Base):
    __tablename__ = 'Newyork'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    price = Column(Integer)
    
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    passwd = Column(String)
    username = Column(String)

    # def __init__(self, email=None, username='Guest'): #None = null value in sql
    #     self.email = email
    #     self.username = username

    # def __repr__(self):
    #     return 'User %s, %r, %r' % (self.id, self.email, self.username)