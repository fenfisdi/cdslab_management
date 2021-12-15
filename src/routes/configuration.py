from fastapi import APIRouter, Depends
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)

from src.interfaces import ConfigurationInterface
from src.models.db_models import Configuration
from src.models.routes import UpdateConfiguration
from src.use_cases import CredentialUseCase
from src.utils.encoder import BsonObject
from src.utils.message import ConfigurationMessage
from src.utils.response import UJSONResponse

configuration_routes = APIRouter(tags=['config'])


@configuration_routes.get('/configuration')
def find_configuration(
    admin=Depends(CredentialUseCase.get_manager)
):
    configuration = ConfigurationInterface.find_one()
    if not configuration:
        configuration = Configuration(
            storage_time=1,
            simulation_removal_before=1,
            simulation_scheduled_removal=1
        )
        try:
            configuration.save()
        except Exception as error:
            return UJSONResponse(str(error), HTTP_400_BAD_REQUEST)

    return UJSONResponse(
        ConfigurationMessage.found,
        HTTP_200_OK,
        BsonObject.dict(configuration)
    )


@configuration_routes.put('/configuration')
def find_configuration(
    configuration: UpdateConfiguration,
    admin=Depends(CredentialUseCase.get_manager)
):
    configuration_found = ConfigurationInterface.find_one()
    if not configuration_found:
        return UJSONResponse(
            ConfigurationMessage.not_found,
            HTTP_400_BAD_REQUEST
        )

    try:
        data = configuration.dict(exclude_none=True)
        if data:
            configuration_found.update(**data)
            configuration_found.reload()
    except Exception as error:
        return UJSONResponse(str(error), HTTP_400_BAD_REQUEST)

    return UJSONResponse(
        ConfigurationMessage.update,
        HTTP_200_OK,
        BsonObject.dict(configuration_found)
    )
