from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime


class Audit(SQLModel, table=True):
    __tablename__ = "audits"
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    date_created: datetime = Field(default=datetime.utcnow())
