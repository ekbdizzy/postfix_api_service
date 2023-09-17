from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.dialects.mysql import TINYINT

from .engine import Base


class Mailbox(Base):
    __tablename__ = 'mailbox'

    username = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)
    maildir = Column(String)
    quota = Column(BigInteger, default=0)
    local_part = Column(String)
    domain = Column(String)
    created = Column(DateTime, default=datetime.now())
    modified = Column(DateTime, default=datetime.now())
    active = Column(TINYINT(), default=1)
    phone = Column(String, default="")
    email_other = Column(String, default="")
    token = Column(String, default="")
    token_validity = Column(DateTime, default=datetime.now())
    password_expiry = Column(DateTime, default=datetime.now() + relativedelta(years=10))


class Alias(Base):
    __tablename__ = 'alias'
    address = Column(String, primary_key=True)
    goto = Column(String)
    domain = Column(String)
    created = Column(DateTime, default=datetime.now())
    modified = Column(DateTime, default=datetime.now())
    active = Column(TINYINT(), default=1)
