from sqlalchemy.orm import Session

from . import models, schemas


def get_audit(db: Session, audit_id: int):
    return db.query(models.Audit).filter(models.Audit.id == audit_id).first()


def get_audits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Audit).offset(skip).limit(limit).all()


def create_audit(db: Session, audit: schemas.AuditCreate):
    db_audit = models.Audit(**audit.dict())
    db.add(db_audit)
    db.commit()
    db.refresh(db_audit)
    return db_audit
