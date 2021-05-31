from src.services import FileAPI, ModelAPI


class PurgeUseCase:

    @classmethod
    def handle(cls, simulation_id: str):
        response, is_invalid = FileAPI.root_delete_file_simulation(
            simulation_id
        )
        if is_invalid:
            return response

        response, is_invalid = ModelAPI.root_delete_simulation(simulation_id)
        if is_invalid:
            return response
