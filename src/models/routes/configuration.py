from pydantic import BaseModel, Field


class UpdateConfiguration(BaseModel):
    storage_time: int = Field(None)
    simulation_removal_before: int = Field(None)
    simulation_scheduled_removal: int = Field(None)
