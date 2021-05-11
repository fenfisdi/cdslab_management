from pydantic import BaseModel, Field

class UpdateTemplate(BaseModel):
    name:str = Field(...)
    content:str = Field(...)

