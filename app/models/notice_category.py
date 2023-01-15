from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.notice import Notice
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class NoticeCategory(Base, TimestampMixin, DeleteTimeMixin):

    box_id = Column(Integer, ForeignKey("box.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    name = Column(String(100))

    notices = relationship(Notice)
