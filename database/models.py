from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Audit(Base):
    __tablename__ = "audits"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    date_created = Column(DateTime)
