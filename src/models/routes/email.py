from pydantic import BaseModel, EmailStr, Field


class EmailNotification(BaseModel):
    template: str = Field(None)
    email: EmailStr = Field(...)
    receiver: str = Field("User")
    subject: str = Field(...)
    message: str = Field(...)
