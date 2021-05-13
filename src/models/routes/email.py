from pydantic import BaseModel, EmailStr, Field


class EmailNotification(BaseModel):
    template: str = Field(...)
    email: EmailStr = Field(...)
    receiver: str = Field(...)
    subject: str = Field(...)
    message: str = Field(..., max_length=64)
