from holvflask.pro_init_db import Base
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, backref

class Country(Base):
    __tablename__ = 'Country'

    def __init__(self, countrycd, countryname):
        self.countrycd = countrycd
        self.countryname = countryname

    id = Column(Integer, primary_key=True)
    countrycd = Column(String)
    countryname = Column(String)

    def json(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
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