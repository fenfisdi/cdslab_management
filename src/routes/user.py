from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from src.models.general import UserRoles
from src.services import UserAPI
from src.use_cases.role import ValidateUserRoles
from src.use_cases.security import SecurityUseCase
from src.utils.message import UserMessage
from src.utils.response import UJSONResponse

user_routes = APIRouter(tags=['User'])


@user_routes.get('/user')
def list_users(name: str):
    """

    :param name:
    """
    response, is_invalid = UserAPI.list_user(name=name)
    if is_invalid:
        return response

    users = response.get('data')

    response, is_invalid = UserAPI.list_user(name=name, role=UserRoles.ADMIN)
    if is_invalid:
        return response

    admins = response.get('data')

    users = [
        {
            'name': user.get('name'),
            'last_name': user.get('last_name'),
            'email': user.get('email'),
            'role': user.get('role')
        } for user in (users + admins)
    ]

    return UJSONResponse(UserMessage.found, HTTP_200_OK, users)


@user_routes.post('/user/{email}/role')
def update_user_role(email: str, role: UserRoles):
    """

    :param email:
    :param role:
    """
    response, is_invalid = UserAPI.find_user(email)
    if is_invalid:
        return response

    response, is_invalid = UserAPI.update_user(email, role)
    if is_invalid:
        return response

    return UJSONResponse(UserMessage.role_updated, HTTP_200_OK)


@user_routes.post('/user/{email}/disable')
def disable_user(email: str, admin=Depends(SecurityUseCase.validate)):
    response, is_invalid = ValidateUserRoles.handle(email, admin)
    if is_invalid:
        return response

    response, is_invalid = UserAPI.disable_user(email)
    if is_invalid:
        return response

    return UJSONResponse(UserMessage.disabled, HTTP_200_OK)


@user_routes.post('/user/{email}/enable')
def enable_user(email: str, admin=Depends(SecurityUseCase.validate)):
    response, is_invalid = ValidateUserRoles.handle(
        email,
        admin,
        is_enabled=False
    )
    if is_invalid:
        return response

    response, is_invalid = UserAPI.enable_user(email)
    if is_invalid:
        return response

    return UJSONResponse(UserMessage.enabled, HTTP_200_OK)
