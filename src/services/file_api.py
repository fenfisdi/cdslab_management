from os import environ

from src.utils.response import to_response
from .service import API, APIService


class FileAPI:
    api_url = environ.get('FILE_API')
    request = APIService(API(api_url))

    @classmethod
    def root_delete_file_simulation(cls, simulation_uuid: str):
        response = cls.request.post(f'/root/simulation/{simulation_uuid}')
        if not response.ok:
            return to_response(response), True
        return response.json(), False
