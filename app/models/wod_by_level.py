from models.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class WodByLevel(Base):

    wod_id = Column(Integer, ForeignKey("wod.id"), nullable=False)
    wod_level_id = Column(Integer, ForeignKey("wod_level.id"), nullable=False)

    content = Column(String(2048))
    record_from_uid = Column(String(255), unique=True)
    ranking_algorithm_uid = Column(String(255), unique=True)
