import datetime
from typing import List

from dateutil.relativedelta import relativedelta

from pydantic import BaseModel


class MailboxData(BaseModel):
    """Model for userdata, which is used to create new mailbox."""
    username: str
    password: str
    name: str
    domain: str
    maildir: str = ""
    quota: int = 0
    active: int = 1
    phone: str = ""
    email_other: str = ""
    token: str = ""
    token_validity: datetime.datetime = datetime.datetime.now()
    password_expiry: datetime.datetime = datetime.datetime.now() + relativedelta(years=10)


class MailboxDataList(BaseModel):
    mailboxes: List[MailboxData]