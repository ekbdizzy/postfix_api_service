from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.dialects.mysql import TINYINT

from .engine import Base


class Mailbox(Base):
    __tablename__ = 'mailbox'

    username = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)
    maildir = Column(String)
    quota = Column(BigInteger)
    local_part = Column(String)
    domain = Column(String)
    created = Column(DateTime)
    modified = Column(DateTime)
    active = Column(TINYINT())
    phone = Column(String)
    email_other = Column(String)
    token = Column(String)
    token_validity = Column(DateTime)
    password_expiry = Column(DateTime)