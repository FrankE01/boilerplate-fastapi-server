from datetime import datetime
import uuid
from uuid_v9 import uuidv9

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TimestampMixin:
    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

class Configurations(Base, TimestampMixin):
    __tablename__ = 'configurations'

    id: Mapped[uuid.UUID] = mapped_column(Integer, primary_key=True, default=uuidv9())
    key: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    value: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f"<Configuration(key={self.key!r}, value={self.value!r})>"
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}