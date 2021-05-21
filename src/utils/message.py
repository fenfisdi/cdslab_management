from dataclasses import dataclass


@dataclass
class UserMessage:
    disabled: str = 'User has been disabled'
    enabled: str = 'User has been enabled'
    invalid_role: str = 'User invalid role'
    role_updated: str = 'User role has been updated'
    found: str = 'User Found'


@dataclass
class SecurityMessage:
    without_privileges: str = 'User without privileges'
    invalid_token: str = 'Invalid Token'


@dataclass
class EmailMessage:
    sent: str = 'Email has been sent'


@dataclass
class TemplateMessage:
    create: str = 'Template has been created'
    update: str = 'Template has been updated'
    exist: str= 'Template exist'
    not_exist: str = 'Template not found'


@dataclass
class ConfigurationMessage:
    found: str = 'Configuration found'
    update: str = 'Configuration updated'
    not_found: str = 'Configuration not found'
