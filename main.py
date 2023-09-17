from fastapi import FastAPI

from database.engine import db_session
from database.models import Mailbox, Alias
from database.pydantic_models import MailboxData
from utils.mailbox_utils import convert_data_to_mailbox, convert_data_to_alias

app = FastAPI()


@app.get("/")
def index():
    return {}


@app.get("/mailbox/")
def get_mailboxes():
    """Get list of all mailboxes"""
    with db_session() as session:
        mailboxes = session.query(Mailbox).all()
    return mailboxes


@app.post("/mailbox/")
def create_mailbox(data: MailboxData):
    """Create mailbox."""
    # TODO check user does not exists.
    with db_session() as session:
        mailbox = convert_data_to_mailbox(data, Mailbox())
        alias = convert_data_to_alias(data, Alias())
        session.add(mailbox)
        session.add(alias)
        session.commit()
        return mailbox


@app.get("/mailboxes/{domain}/")
def get_mailboxes_by_domain(domain):
    """Get list of mailboxes filtered by domain."""
    with db_session() as session:
        mailboxes = session.query(Mailbox).filter_by(domain=domain).all()
    return mailboxes


@app.get("/aliases/")
def get_aliases():
    with db_session() as session:
        aliases = session.query(Alias).all()
        return aliases
