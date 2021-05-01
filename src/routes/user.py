from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from src.services import UserAPI
from src.use_cases.role import ValidateUserRoles
from src.use_cases.security import SecurityUseCase
from src.utils.message import UserMessage
from src.utils.response import UJSONResponse

user_routes = APIRouter(tags=['User'])


@user_routes.post('/user/disable')
def disable_user(email: str, admin=Depends(SecurityUseCase.validate)):
    response, is_invalid = ValidateUserRoles.handle(email, admin)
    if is_invalid:
        return response

    response, is_invalid = UserAPI.disable_user(email)
    if is_invalid:
        return response

    return UJSONResponse(UserMessage.disabled, HTTP_200_OK)


@user_routes.post('/user/enable')
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
