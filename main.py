from fastapi import FastAPI

from database.engine import session
from database.models import Mailbox

app = FastAPI()

@app.get("/")
async def index():
    return {}


@app.get("/mailboxes/")
async def get_mailboxes():
    """Get list of all mailboxes"""

    mailboxes = session.query(Mailbox).first()
    print(mailboxes)
    return mailboxes
