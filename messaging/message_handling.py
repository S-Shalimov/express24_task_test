import logging
import logging.config
from typing import Tuple

from messaging.message_interface import MessageInterface
from messaging.messengers.messenger_interface import MessengerInterface
from messaging.messengers.telegram import TelegramMessenger
from messaging.messengers.whatsapp import WhatsAppMessenger

from config.general import ProjectPaths


class MessageHandler:
    def __init__(self):
        logging.config.fileConfig(ProjectPaths.BASE_LOG_CONFIG, disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)

    """
    A decorator to handle exceptions and log errors.

    :param func: The method to be decorated
    :return: Wrapped method that handles exceptions
    """
    def _handle_exceptions(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (RemoteServiceException, RemoteValidationException) as remote_exc:
                self.logger.error("Remote service error: %s", remote_exc)
                return f"Remote service error: {remote_exc}"
            except (TypeError, ValueError) as exc:
                self.logger.error("Validation error: %s", exc)
                return f"Validation error: {exc}"
            except Exception as exc:
                self.logger.error("Other error: %s", exc)
                return f"Other error: {exc}"
        return wrapper

    """
    Get the type and text of the message from the payload.

    :param payload: MessageInterface instance
    :return: Tuple containing message type and text
    :rtype: tuple[str, str]
    :raises Exception: If there's an error getting message data
    """
    def _get_message_data(self, payload: MessageInterface) -> Tuple[str, str]:

        try:
            message_type = payload.get_type()
            message_text = payload.get_message()
            return message_type, message_text
        except (TypeError, ValueError) as exc:
            raise Exception(f"Error while getting message data: {exc}")

    """
    Get the messenger instance based on the message type.

    :param message_type: Type of the message
    :return: Messenger instance
    :rtype: MessengerInterface
    :raises ValueError: If the message type is unknown
    """
    def _get_messenger(self, message_type: str) -> MessengerInterface:

        match message_type:
            case "telegram":
                return TelegramMessenger()
            case "whatsapp":
                return WhatsAppMessenger()
            case _:
                raise ValueError(f"Unknown message type: {message_type}")

    """
    Handle the message payload and send the message using the appropriate messenger.

    :param payload: MessageInterface instance
    :return: Response from the messaging service or an error message
    :rtype: str | None
    """
    @_handle_exceptions
    def handle(self, payload: MessageInterface) -> str | None:
        message_type, message_text = self._get_message_data(payload)
        messenger = self._get_messenger(message_type)
        response = messenger.send(message_text)
        return response