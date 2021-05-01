from dataclasses import dataclass


@dataclass
class UserMessage:
    disabled: str = 'User has been disabled'
    enabled: str = 'User has been enabled'
    invalid_role: str = 'User invalid role'


@dataclass
class ValidationMessage:
    invalid_user: str = ''
    invalid_token: str = ''


@dataclass
class SecurityMessage:
    invalid_token: str = 'Invalid Token'
