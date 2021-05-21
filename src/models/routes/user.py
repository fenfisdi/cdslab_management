from pydantic import BaseModel, EmailStr, Field

from src.models.general import UserRoles


class UpdateUserEnable(BaseModel):
    email: EmailStr = Field(...)
    is_enabled: bool = Field(...)


class UpdateUserRole(BaseModel):
    email: EmailStr = Field(...)
    role: UserRoles = Field(...)
