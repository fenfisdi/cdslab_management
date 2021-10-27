from os import environ

from src.utils.response import to_response
from .service import API, APIService


class ModelAPI:
    api_url = environ.get('MODEL_API')
    request = APIService(API(api_url))

    @classmethod
    def find_simulation_expired(cls, days_expired: int):
        parameters = {
            'to_expire': days_expired,
        }
        response = cls.request.get(
            f'/root/simulation/expired',
            parameters=parameters
        )
        if not response.ok:
            return to_response(response), True
        return response.json(), False

    @classmethod
    def root_delete_simulation(cls, simulation_id: str):
        response = cls.request.get(f'/root/simulation/{simulation_id}')
        if not response.ok:
            return to_response(response), True
        return response.json(), False
