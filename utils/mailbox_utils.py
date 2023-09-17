import bcrypt
from sqlalchemy.orm import Session

from database.models import Mailbox, Alias
from database.pydantic_models import MailboxData


def encrypt_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')


def convert_data_to_mailbox(data: MailboxData, mailbox: Mailbox) -> Mailbox:
    """Convert data from request to Mailbox model."""
    mailbox.username = f"{data.username}@{data.domain}"
    mailbox.name = data.name
    mailbox.password = encrypt_password(data.password)
    mailbox.maildir = f"{data.domain}/{data.username}/"
    mailbox.quota = data.quota
    mailbox.local_part = data.username
    mailbox.domain = data.domain
    mailbox.active = data.active
    mailbox.phone = data.phone
    mailbox.email_other = data.email_other
    mailbox.token = data.token
    mailbox.token_validity = data.token_validity
    mailbox.password_expiry = data.password_expiry
    return mailbox


def convert_data_to_alias(data: MailboxData, alias: Alias):
    """Convert data from request to Mailbox Alias model."""
    alias.address = f"{data.username}@{data.domain}"
    alias.goto = f"{data.username}@{data.domain}"
    alias.domain = data.domain
    alias.active = data.active
    return alias


def create_mailbox(session: Session, data: MailboxData):
    """Create a new mailbox."""
    mailbox = convert_data_to_mailbox(data, Mailbox())
    alias = convert_data_to_alias(data, Alias())
    session.add(mailbox)
    session.add(alias)
    session.commit()
    return mailbox
