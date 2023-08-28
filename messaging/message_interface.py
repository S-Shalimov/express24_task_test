from abc import ABC, abstractmethod


class MessageInterface(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_message(self) -> str:
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