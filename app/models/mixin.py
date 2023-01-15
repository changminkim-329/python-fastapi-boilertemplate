from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)


class DeleteTimeMixin:
    deleted_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False)
