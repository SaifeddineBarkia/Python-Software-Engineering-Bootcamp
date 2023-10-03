import datetime

from models.base import Base
from sqlalchemy import Column,  Integer, UniqueConstraint, TIMESTAMP, ForeignKeyConstraint, Index

class LikedPost(Base):
    __tablename__ = 'liked_post'

    __table_args__ = (UniqueConstraint("user_id","post_id",name="user_post_unique"),
                      ForeignKeyConstraint(["user_id"],["user.id"]),)
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)

Index("liked_post_user_id_idx", LikedPost.user_id) # to access the column value