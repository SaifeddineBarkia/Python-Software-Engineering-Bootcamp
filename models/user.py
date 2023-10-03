import datetime

from models.base import Base
from sqlalchemy import Column, String, Integer, UniqueConstraint, TIMESTAMP

class User(Base):
    __tablename__ = 'user'

    __table_args__ = (UniqueConstraint("username",name="username_unique"),)
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    username = Column(String(20))
    short_description = Column(String)
    long_bio = Column(String)
