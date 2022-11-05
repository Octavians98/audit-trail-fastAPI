from typing import Union
from datetime import datetime

from pydantic import BaseModel


class AuditBase(BaseModel):
    content: str
    date_created: datetime = datetime.utcnow()


class AuditCreate(AuditBase):
    pass


class AuditModel(AuditBase):
    id: int

    class Config:
        orm_mode = True
