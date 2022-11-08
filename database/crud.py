from sqlmodel import Session, select

from . import models, database


def get_audit(audit_id: int):
    with Session(database.engine) as session:
        audit = session.exec(select(models.Audit).filter(
            models.Audit.id == audit_id)).first()
        return audit


def get_audits(skip: int = 0, limit: int = 100):
    with Session(database.engine) as session:
        audits = session.exec(
            select(models.Audit).offset(skip).limit(limit)).all()
        return audits


def create_audit(audit: models.Audit):

    with Session(database.engine) as session:
        session.add(audit)
        session.commit()
        session.refresh(audit)
        return audit
