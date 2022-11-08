from fastapi import FastAPI, HTTPException

from database.crud import get_audit, get_audits, create_audit
from database.models import Audit
from database.database import create_db_and_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/audits/{audit_id}")
def read_audit(audit_id: int):
    db_audit = get_audit(audit_id=audit_id)
    if db_audit is None:
        raise HTTPException(status_code=404, detail="Audit not found")
    return db_audit


@app.get("/audits/")
def read_audits(skip: int = 0, limit: int = 100):
    audits: list = get_audits(skip=skip, limit=limit)
    if len(audits) == 0:
        raise HTTPException(status_code=404, detail="Audits not found")
    return audits


@app.post("/audits/")
def create_new_audit(audit: Audit):
    return create_audit(audit=audit)
