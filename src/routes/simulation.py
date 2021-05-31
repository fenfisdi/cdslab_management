from fastapi import APIRouter, BackgroundTasks

from src.services import FileAPI, ModelAPI

root_routes = APIRouter(prefix='/root', tags=['Root'], include_in_schema=False)


@root_routes.post('/simulation/expired')
def delete_simulation_expired(background_tasks: BackgroundTasks):
    param = 30
    response, is_invalid = ModelAPI.find_simulation_expired(-param)
    if is_invalid:
        return response

    data = response.get('data')

    for simulation in data:
        simulation_id = simulation.get('identifier')
        response, is_invalid = FileAPI.root_delete_file_simulation(
            simulation_id
        )

        response, is_invalid = ModelAPI.root_delete_simulation(simulation_id)
        pass

    # TODO: List all simulation expired
    pass
