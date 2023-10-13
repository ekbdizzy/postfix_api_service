from environs import Env
from pydantic_settings import BaseSettings


env = Env()
env.read_env()


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = env.str("DB_URL")
    MAILBOXES_PATH: str = env.str("MAILBOXES_PATH")
