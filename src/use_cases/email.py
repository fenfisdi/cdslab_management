from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from smtplib import SMTP

from jinja2 import Template

from src.interfaces.template_interface import TemplateInterface
from src.models.routes import EmailNotification


class EmailUseCase:

    @classmethod
    def render_notification_email(cls, notification: EmailNotification) -> str:
        """
        Render notification

        :param notification:
        """
        template_bd = TemplateInterface.find_one().content
        template_bd = "<html><body><p>{{ message }}</p></body></html>"

        content = Template(template_bd)
        data = dict(
            message=notification.message
        )
        result = content.render(data)
        return result

    @classmethod
    def send_email(cls, email: str, notification: EmailNotification):
        smtp_host = environ.get('SMTP_HOST', 'localhost')
        smtp_port = environ.get('SMTP_PORT', 25)
        smtp_sender = environ.get('SMTP_SENDER')

        message = MIMEMultipart("alternative")
        attach = MIMEText(email, 'html')
        message["Subject"] = notification.subject
        message["From"] = smtp_sender
        message["To"] = notification.email
        message.attach(attach)

        with SMTP(smtp_host, smtp_port) as server:

            server.sendmail(
                smtp_sender,
                notification.email,
                message.as_string()
            )
