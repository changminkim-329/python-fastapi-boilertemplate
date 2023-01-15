from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.user import User
from models.wod_by_level import WodByLevel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class WodLevel(Base, TimestampMixin, DeleteTimeMixin):

    box_id = Column(Integer, ForeignKey("box.id"), nullable=False)
    # user_id = Column(Integer, ForeignKey("user.id"),nullable=False)

    name = Column(String(255))
    level_no = Column(Integer)

    users = relationship(User)
    wod_by_levels = relationship(WodByLevel)
