from fastapi import FastAPI

from database.engine import db_session
from database.models import Mailbox

app = FastAPI()

@app.get("/")
def index():
    return {}


@app.get("/mailboxes/")
def get_mailboxes():
    """Get list of all mailboxes"""
    with db_session() as session:
        mailboxes = session.query(Mailbox).first()
    return mailboxes


