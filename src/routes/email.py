from fastapi import APIRouter, BackgroundTasks, Depends
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)

from src.interfaces.template_interface import TemplateInterface
from src.models.db_models.template import Template
from src.models.routes import EmailNotification, UpdateTemplate
from src.use_cases import CredentialUseCase
from src.use_cases.email import EmailUseCase
from src.utils.encoder import BsonObject
from src.utils.message import EmailMessage, TemplateMessage
from src.utils.response import UJSONResponse

email_routes = APIRouter(tags=['email'])


@email_routes.post('/email/notification')
def send_notification_email(
    notification: EmailNotification,
    task: BackgroundTasks
):
    """
    Send an email with the content of the data in the notification model

    \f
    param notification: Data of the email
    """

    output = EmailUseCase.render_notification_email(notification)
    task.add_task(EmailUseCase.send_email, output, notification)

    return UJSONResponse(EmailMessage.sent, HTTP_200_OK)


@email_routes.put('/email/template')
def update_template(
    template: UpdateTemplate,
    admin=Depends(CredentialUseCase.get_root)
):
    """
    Update a template

    \f
    param template: Template data to update
    """

    template_found = TemplateInterface.find_one()
    if not template_found:
        return UJSONResponse(TemplateMessage.not_exist, HTTP_400_BAD_REQUEST)
    try:
        template_found.update(**template.dict(exclude_none=True))
    finally:
        template_found.reload()

    return UJSONResponse(
        TemplateMessage.update,
        HTTP_200_OK,
        BsonObject.dict(template_found)
    )


@email_routes.get('/email/template')
def find_template(
    admin=Depends(CredentialUseCase.get_root)
):
    """
    Find and return default email template

    """
    template = TemplateInterface.find_one()
    if not template:
        template = Template()
        try:
            template.save()
        except Exception as error:
            return UJSONResponse(str(error), HTTP_400_BAD_REQUEST)

    return UJSONResponse(
        TemplateMessage.found,
        HTTP_200_OK,
        BsonObject.dict(template)
    )
