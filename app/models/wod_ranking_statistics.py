from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.wod_record import WodRecord
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship


class WodRankingStatistics(Base, TimestampMixin, DeleteTimeMixin):

    wod_id = Column(Integer, ForeignKey("wod.id"), nullable=False)
    wod_record_id = Column(Integer, ForeignKey("wod_record.id"), nullable=False)

    ranking_no = Column(Integer, unique=True)

    wod_record = relationship(
        WodRecord, back_populates="wod_ranking_statistics"
    )
