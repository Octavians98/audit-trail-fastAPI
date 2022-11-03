from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Audit(BaseModel):
    id: int
    date_created: datetime
    content: str


store = {1: Audit(id=1, date_created=datetime.utcnow(), content="first audit")}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/audit/{audit_id}")
def read_audit(audit_id: int):
    try:
        return store[audit_id]
    except KeyError:
        return None


@app.get("/audit/")
def read_all_audit():
    return list(store.values())


@app.post("/audit/")
def create_audit(audit: Audit):
    store[audit.id] = audit
    return audit
