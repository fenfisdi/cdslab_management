from .configuration import configuration_routes
from .email import email_routes
from .simulation import root_routes
from .user import user_routes

__all__ = ['user_routes', 'email_routes', 'root_routes', 'configuration_routes']
