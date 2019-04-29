from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


mysql_url = "mysql+pymysql://" + os.getenv('mysql_user') + ":" + os.getenv('mysql_pw') + "@" + os.getenv('mysql_host') + "/projectdb?charset=utf8"

engine = create_engine(mysql_url, echo=True, convert_unicode=True)


# Declare & create Session
db_session = scoped_session( sessionmaker(autocommit=False, autoflush=False, bind=engine) )

Base = declarative_base()
Base.query = db_session.query_property()

def init_database():
    Base.metadata.create_all(bind=engine)

