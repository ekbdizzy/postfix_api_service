from environs import Env

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env = Env()
env.read_env()
SQLALCHEMY_DATABASE_URL = env.str("DB_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
session = session()