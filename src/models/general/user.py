from enum import Enum, unique


@unique
class UserRoles(Enum):
    USER: str = 'user'
    ADMIN: str = 'admin'
