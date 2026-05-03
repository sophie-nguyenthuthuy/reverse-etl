from .base import BaseDestination
from .slack import SlackDestination
from .email import EmailDestination
from .salesforce import SalesforceDestination
from .hubspot import HubSpotDestination

DESTINATION_REGISTRY: dict[str, type[BaseDestination]] = {
    "slack": SlackDestination,
    "email": EmailDestination,
    "salesforce": SalesforceDestination,
    "hubspot": HubSpotDestination,
}

__all__ = [
    "BaseDestination",
    "SlackDestination",
    "EmailDestination",
    "SalesforceDestination",
    "HubSpotDestination",
    "DESTINATION_REGISTRY",
]
