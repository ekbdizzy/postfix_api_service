from fastapi import FastAPI

from database.engine import db_session
from database.models import Mailbox, Alias
from database.pydantic_models import MailboxData, MailboxDataList
from utils import mailbox_utils as utils

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

    with db_session() as session:
        mailbox = session.query(Mailbox).filter_by(username=f"{data.username}@{data.domain}").first()
        if mailbox:
            return {
                "error": "User already exists."
            }
        mailbox = utils.create_mailbox(session, data)
        return mailbox


@app.post("/mailbox/bulk_create/")
def bulk_create_mailboxes(data: MailboxDataList):
    with db_session() as session:
        for mailbox in data.mailboxes:
            utils.create_mailbox(session, mailbox)
    return data.mailboxes


@app.delete("/mailbox/")
def delete_mailbox(email: str):
    # TODO delete folder with letters
    with db_session() as session:
        mailbox = session.query(Mailbox).get(email)
        if mailbox:
            alias = session.query(Alias).get(email)
            session.delete(mailbox)
            session.delete(alias)
            session.commit()
        else:
            return {"error": f"{email} does not exists."}
        return {}


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
