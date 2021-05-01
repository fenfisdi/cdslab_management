from typing import Tuple, Optional, Any

from src.services import UserAPI
from src.utils.message import UserMessage
from src.utils.response import UJSONResponse


class ValidateUserRoles:
    roles = {
        'user': [],
        'admin': ['user'],
        'root': ['user', 'admin'],
    }

    @classmethod
    def handle(
        cls,
        user_email: str,
        admin: dict,
        is_enabled: bool = True
    ) -> Tuple[Optional[Any], bool]:
        response, is_invalid = UserAPI.find_user(
            user_email,
            is_enabled=is_enabled
        )
        if is_invalid:
            return response, True

        user_found = response.get('data')
        user_role = user_found.get('role')
        admin_role = admin.get('role')

        if user_role not in cls.roles.get(admin_role):
            return UJSONResponse(UserMessage.invalid_role, 400), True
        return None, False
