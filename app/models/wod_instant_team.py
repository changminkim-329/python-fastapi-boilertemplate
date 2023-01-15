from models.base_class import Base
from models.wod_record import WodRecord
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class WodInstantTeam(Base):

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    wod_record_id = Column(Integer, ForeignKey("wod_record.id"), nullable=False)

    wod_records = relationship(WodRecord, back_populates="wod_instant_team")
