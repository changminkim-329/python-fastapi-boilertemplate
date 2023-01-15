from datetime import datetime

from models.base_class import Base
from models.mixin import DeleteTimeMixin, TimestampMixin
from models.user import User
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class UserGrade(Base, TimestampMixin, DeleteTimeMixin):

    name = Column(String(50))
    description = Column(String(255))

    users = relationship(User)
