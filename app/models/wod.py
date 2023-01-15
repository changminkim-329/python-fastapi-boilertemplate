from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.wod_by_level import WodByLevel
from models.wod_ranking_statistics import WodRankingStatistics
from models.wod_record import WodRecord
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Wod(Base, TimestampMixin, DeleteTimeMixin):

    box_id = Column(Integer, ForeignKey("box.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    title = Column(String(100))
    explanation = Column(String(255))
    wod_date = Column(DateTime)
    is_exposed = Column(Boolean, default=True)

    wod_records = relationship(WodRecord)
    wod_ranking_statistics = relationship(WodRankingStatistics)
    wod_by_levels = relationship(WodByLevel)
