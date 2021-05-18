from os import environ
from typing import Optional, Tuple, Union

from src.models.general import UserRoles
from src.utils.response import UJSONResponse
from src.utils.response import to_response
from .service import API, APIService


class UserAPI:
    api_url = environ.get('USER_API')
    request = APIService(API(api_url))

    @classmethod
    def find_user(
        cls,
        email: str,
        is_valid: bool = True,
        is_enabled: bool = True
    ) -> Tuple[Union[dict, UJSONResponse], bool]:
        """

        :param email:
        :param is_valid:
        :param is_enabled:
        """
        parameters = {
            'is_valid': is_valid,
            'is_enabled': is_enabled,
        }
        response = cls.request.get(f'/user/{email}', parameters=parameters)
        if not response.ok:
            return to_response(response), True
        return response.json(), False

    @classmethod
    def list_user(
        cls,
        name: Optional[str] = None,
        role: UserRoles = UserRoles.USER
    ):
        """

        :param name:
        :param role:
        """
        parameters = {
            'role': role.value,
            'is_valid': True,
        }
        if name:
            parameters['name'] = name
        response = cls.request.get(f'/user', parameters=parameters)
        if not response.ok:
            return to_response(response), True
        return response.json(), False

    @classmethod
    def disable_user(
        cls,
        email: str
    ) -> Tuple[Union[dict, UJSONResponse], bool]:
        response = cls.request.post(f'/user/{email}/disable')

        if not response.ok:
            return to_response(response), True
        return response.json(), False

    @classmethod
    def enable_user(
        cls,
        email: str
    ) -> Tuple[Union[dict, UJSONResponse], bool]:
        response = cls.request.post(f'/user/{email}/enable')

        if not response.ok:
            return to_response(response), True
        return response.json(), False

    @classmethod
    def update_user(cls, email: str, role: UserRoles):
        data = {
            'role': role.value
        }
        response = cls.request.put(f'/user/{email}', data=data)

        if not response.ok:
            return to_response(response), True
        return response.json(), False

