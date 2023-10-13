import contextlib

from environs import Env

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings()
print(settings.SQLALCHEMY_DATABASE_URL)

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)


@contextlib.contextmanager
def db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
