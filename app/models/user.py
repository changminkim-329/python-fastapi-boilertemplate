from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.notice import Notice
from models.notice_category import NoticeCategory
from models.wod import Wod
from models.wod_instant_team import WodInstantTeam
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from .const import GenderType, JoinType


class User(Base, TimestampMixin, DeleteTimeMixin):

    user_grade_id = Column(Integer, ForeignKey("user_grade.id"), nullable=False)
    box_id = Column(Integer, ForeignKey("box.id"), default=1)
    wod_level_id = Column(Integer, ForeignKey("wod_level.id"), nullable=True)

    email = Column(String(100), unique=True, nullable=False, index=True)
    nickname = Column(String(100), unique=True)
    hashed_pw = Column(String(2000), nullable=False)
    cellphone = Column(String(50))
    join_type = Column(Enum(JoinType))
    name = Column(String(50))
    gender = Column(Enum(GenderType))
    birth_year = Column(DateTime)
    height = Column(Integer)
    weight = Column(Integer)

    # todo - wod_team
    # one_to_one : 단수, 나머지: 복수
    wod_instant_teams = relationship(WodInstantTeam)
    wods = relationship(Wod)
    notices = relationship(Notice)
    notice_categorys = relationship(NoticeCategory)
