from typing import List, Optional

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from src.models.general import UserRoles
from src.models.routes import UpdateUserEnable, UpdateUserRole
from src.services import UserAPI
from src.use_cases import CredentialUseCase
from src.utils.message import UserMessage
from src.utils.response import UJSONResponse

user_routes = APIRouter(tags=['User'])


@user_routes.get('/user')
def list_users(
    name: Optional[str] = None,
    admin=Depends(CredentialUseCase.get_manager)
):
    """

    :param admin:
    :param name:
    """
    response, is_invalid = UserAPI.list_user(name=name)
    if is_invalid:
        return response
    users_enabled = response.get('data')

    response, is_invalid = UserAPI.list_user(name=name, is_enabled=False)
    if is_invalid:
        return response
    users_disabled = response.get('data')

    response, is_invalid = UserAPI.list_user(name=name, role=UserRoles.ADMIN)
    if is_invalid:
        return response
    admins_enabled = response.get('data')

    response, is_invalid = UserAPI.list_user(
        name=name,
        role=UserRoles.ADMIN,
        is_enabled=False
    )
    if is_invalid:
        return response
    admins_disabled = response.get('data')

    users = users_enabled + users_disabled + admins_enabled + admins_disabled

    result = [
        {
            'name': user.get('name'),
            'last_name': user.get('last_name'),
            'email': user.get('email'),
            'role': user.get('role'),
            'is_enabled': user.get('is_enabled')
        } for user in users
        if user.get('email') != admin.get('email')
    ]

    return UJSONResponse(UserMessage.found, HTTP_200_OK, result)


@user_routes.post('/user/role')
def update_user_role(
    users: List[UpdateUserRole],
    admin=Depends(CredentialUseCase.get_manager)
):
    """

    :param users:
    :param admin:
    """

    for user in users:
        UserAPI.update_user(user.email, user.role)

    return UJSONResponse(UserMessage.role_updated, HTTP_200_OK)


@user_routes.post('/user/enable')
def update_user_enabled(
    users: List[UpdateUserEnable],
    admin=Depends(CredentialUseCase.get_root)
):
    """

    :param users:
    :param admin:
    """
    for user in users:
        if user.is_enabled:
            UserAPI.enable_user(user.email)
        else:
            UserAPI.disable_user(user.email)
    return UJSONResponse(UserMessage.enabled, HTTP_200_OK)
