from datetime import datetime
from typing import TYPE_CHECKING

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.wod_instant_team import WodInstantTeam
from models.wod_ranking_statistics import WodRankingStatistics
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class WodRecord(Base, TimestampMixin, DeleteTimeMixin):
    wod_id = Column(Integer, ForeignKey("wod.id"), nullable=False)

    register = Column(Integer)
    mango_record_uid = Column(String(255), unique=True, nullable=False)

    wod_instant_team = relationship(
        WodInstantTeam, back_populates="wod_records"
    )
    wod_ranking_statistics = relationship(
        WodRankingStatistics, back_populates="wod_record", uselist=False
    )

    # WodInstantTeam -> "WodInstantTeam", WodRankingStatics -> "WodRankingStatics"
