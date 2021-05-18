from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from smtplib import SMTP
from string import Template

from src.interfaces.template_interface import TemplateInterface
from src.models.routes import EmailNotification


class EmailUseCase:

    @classmethod
    def render_notification_email(cls, notification: EmailNotification) -> str:
        """
        Render notification

        :param notification:
        """
        template_bd = TemplateInterface.find_one(
            name=notification.template
        ).content
        content = Template(template_bd)
        return content.substitute(message=notification.message)

    @classmethod
    def send_email(cls, email: str, notification: EmailNotification):
        smtp_host = environ.get('SMTP_HOST')
        smtp_port = environ.get('SMTP_PORT')
        smtp_sender = environ.get('SMTP_SENDER')

        message = MIMEMultipart("alternative")
        attach = MIMEText(email, 'html')
        message["Subject"] = notification.subject
        message["From"] = smtp_sender
        message["To"] = notification.email

        with SMTP(smtp_host, smtp_port) as server:
            message.attach(attach)
            server.sendmail(
                smtp_sender,
                notification.email,
                message.as_string()
            )
