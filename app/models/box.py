from datetime import datetime
from typing import TYPE_CHECKING

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.notice import Notice
from models.notice_category import NoticeCategory
from models.user import User
from models.wod import Wod
from models.wod_level import WodLevel
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class Box(Base, TimestampMixin, DeleteTimeMixin):

    name = Column(String(50))
    address = Column(String(255))
    phone = Column(String(50))
    description = Column(String(255))

    users = relationship(User)
    wods = relationship(Wod)
    wod_levels = relationship(WodLevel)
    notices = relationship(Notice)
    notice_categorys = relationship(NoticeCategory)
