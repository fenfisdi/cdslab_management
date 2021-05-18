from typing import List, Optional, Union

from fastapi.exceptions import HTTPException as FastApiException
from fastapi.responses import UJSONResponse as FastAPIResponse
from requests.models import Response


class UJSONResponse(FastAPIResponse):
    def __init__(
            self,
            message: str,
            status_code: int,
            data: Optional[Union[dict, List[dict]]] = None):
        response = dict(
            message=message,
            status_code=status_code,
            data=data,
        )
        super().__init__(response, status_code)


class HTTPException(FastApiException):

    def __init__(self, message: str, status_code: int, data: dict = None):
        response = dict(
            message=message,
            status_code=status_code,
            data=data,
        )
        super().__init__(status_code, response, headers=None)


def to_response(response: Response) -> UJSONResponse:
    data = response.text
    message = 'API Error'
    if response.headers.get('content-type') == 'application/json':
        data = response.json()
        message = data.get('message', message)
        data = data.get('data', data)
    return UJSONResponse(message, response.status_code, data)
