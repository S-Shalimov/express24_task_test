class TelegramMessenger(MessengerInterface):
    """
    Send a message to Telegram

    :return: Return a string response from remote service
    :rtype: str
    :raises RemoteServiceException:
    :raises RemoteValidationException:
    """
    def send(self, message: str) -> str:
        # let's assume we have code here
        pass

class Payload(MessageInterface):
    def __init__(self):
        self.message_type = None

    """
    Get type of the message

    :return: Eg "telegram", "whatsapp", "push"
    :rtype: str
    :raises TypeError: Unknown type in Payload
    """
    def get_type(self) -> str:
        # let's assume we have code here
        pass

    """
    Get message text

    :return: Message text
    :rtype: str
    :raises ValueError: Could not get a message from Payload
    """
    def get_message(self) -> str:
        # and here
        pass

class MessageHandler:
    """
    Handle a payload, send the message and return result
    """
    def handle(self, payload: MessageInterface):
        # your code goes here
        pass
