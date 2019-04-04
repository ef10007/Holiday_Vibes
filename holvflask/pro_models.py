from holvflask.pro_init_db import Base
from sqlalchemy import Column, Integer, Float, String, DateTime, TIMESTAMP, ForeignKey, PrimaryKeyConstraint, func
from sqlalchemy.orm import relationship, backref

class Preference(Base):
    __tablename__ = 'Preference'
    
    def __init__(self, userid, cityname, temperature, minbud, maxbud):
        self.userid = userid
        self.cityname = cityname
        self.temperature = temperature
        self.minbud = minbud
        self.maxbud = maxbud

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('User.id'))
    cityname = Column(String)
    temperature = Column(Integer)
    minbud = Column(Integer)
    maxbud = Column(Integer)
    useridfk = relationship('User')

    def __repr__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.userid, self.cityname, self.temperature, self.minbud, self.maxbud, self.useridfk.username)

    def json(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

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
    email = Column(String, unique=True)
    passwd = Column(String)
    username = Column(String)
    registdate = Column(TIMESTAMP)

    def __init__(self, email, passwd, username='Guest', makeSha=True):


        self.email = email

        if makeSha:
            self.passwd = func.sha2(passwd, 256)
        else:
            self.passwd = passwd

        self.username = username

        print("----------------------", email)

    def __repr__(self):
        return 'User details : %s, %s, %s' % (self.username, self.email, self.passwd)