from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# postgres connection
username = 'postgres'
password = 'pass'
SQLALCHEMY_DATABASE_URL = "postgresql://" + username + ":" + password + "@localhost/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
