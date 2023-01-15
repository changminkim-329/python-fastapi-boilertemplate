from enum import Enum


class JoinType(str, Enum):
    KAKAO = "KAKAO"
    APPLE = "APPLE"
    EMAIL = "EMAIL"


class GenderType(str, Enum):
    M = "M"
    F = "F"
