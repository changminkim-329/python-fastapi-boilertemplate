# Import all the models, so that Base has them before being
# imported by Alembic
from models.base_class import Base
from models.box import Box
from models.notice import Notice
from models.notice_category import NoticeCategory
from models.user import User
from models.user_grade import UserGrade
from models.wod import Wod
from models.wod_by_level import WodByLevel
from models.wod_instant_team import WodInstantTeam
from models.wod_level import WodLevel
from models.wod_ranking_statistics import WodRankingStatistics
from models.wod_record import WodRecord
