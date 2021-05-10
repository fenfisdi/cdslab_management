from fastapi import APIRouter, BackgroundTasks
from starlette.status import HTTP_200_OK

from src.models.routes import EmailNotification
from src.use_cases.email import EmailUseCase
from src.utils.message import EmailMessage
from src.utils.response import UJSONResponse

email_routes = APIRouter(tags=['tags'])


@email_routes.post('/email/notification')
def send_notification_email(
    notification: EmailNotification,
    task: BackgroundTasks
):
    output = EmailUseCase.render_notification_email(notification)
    task.add_task(EmailUseCase.send_email, output, notification)

    return UJSONResponse(EmailMessage.sent, HTTP_200_OK)
