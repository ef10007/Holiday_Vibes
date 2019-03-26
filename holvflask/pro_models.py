from holvflask.pro_init_db import Base
from sqlalchemy import Column, Integer, Float, String, DateTime, TIMESTAMP, ForeignKey, PrimaryKeyConstraint, func
from sqlalchemy.orm import relationship, backref

class Country(Base):
    __tablename__ = 'Country'
    
    def __init__(self, countryname, countrycode):
        self.countryname = countryname
        self.countrycode = countrycode

    id = Column(Integer, primary_key=True)
    countryname = Column(String)
    countrycode = Column(String)


    def json(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class CityMPT(Base):
    __tablename__ = 'CityMPT'

    def __init__(self, mpt_citycode, mpt_cityname, mpt_countrycode):
        self.mpt_citycode = mpt_citycode
        self.mpt_cityname = mpt_cityname
        self.mpt_countrycode = mpt_countrycode

    mpt_citycode = Column(String, primary_key=True)
    mpt_cityname = Column(String)
    mpt_countrycode = Column(String, ForeignKey('Country.countrycode'))
    mpt_countrycd = relationship('Country')

    def json(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class City(Base):
    __tablename__ = 'City'

    def __init__(self, citycode, cityname, countrycode):
        self.citycode = citycode
        self.cityname = cityname
        self.countrycode = countrycode

    citycode = Column(String, primary_key=True)
    cityname = Column(String)
    countrycode = Column(String, ForeignKey('Country.countrycode'))
    countrycd = relationship('Country')

    def json(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String, unique=True)
    passwd = Column(String)
    createdate = Column(TIMESTAMP)

    def __init__(self, email=None, passwd=None, username='Guest', makeSha=False):

        self.email = email

        if makeSha:
            self.passwd = func.sha2(passwd, 256)
        else:
            self.passwd = passwd

        self.username = username

    def __repr__(self):
        return 'User %s, %r, %r' % (self.id, self.email, self.username)