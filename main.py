from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session

from database.crud import get_audit, get_audits, create_audit
from database.models import Audit
from database.schemas import AuditCreate, AuditModel
from database.database import Base, SessionLocal, engine


def create_tables():
    Base.metadata.create_all(bind=engine)

# Dependency


def start_application():
    app = FastAPI()
    create_tables()
    return app


app = start_application()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Audit(BaseModel):
    id: int
    date_created: datetime
    content: str


store = {1: Audit(id=1, date_created=datetime.utcnow(), content="first audit")}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/audit/{audit_id}", response_model=AuditModel)
def read_audit(audit_id: int, db: Session = Depends(get_db)):
    db_audit = get_audit(db, audit_id=audit_id)
    if db_audit is None:
        raise HTTPException(status_code=404, detail="Audit not found")
    return db_audit


@app.get("/audits/", response_model=list[AuditModel])
def read_audits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    audits: list = get_audits(db, skip=skip, limit=limit)
    if len(audits) == 0:
        raise HTTPException(status_code=404, detail="Audits not found")
    return audits


@app.post("/audit/", response_model=AuditModel)
def create_new_audit(audit: AuditCreate, db: Session = Depends(get_db)):
    print("Audit", audit)
    return create_audit(db=db, audit=audit)
