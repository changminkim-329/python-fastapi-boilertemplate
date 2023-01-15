from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String


class Notice(Base, TimestampMixin, DeleteTimeMixin):

    notice_category_id = Column(
        Integer, ForeignKey("notice_category.id"), nullable=False
    )
    box_id = Column(Integer, ForeignKey("box.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    title = Column(String(200))
    content = Column(String(255))
    is_exposed = Column(Boolean, default=True)
    the_top = Column(Boolean, default=False)
