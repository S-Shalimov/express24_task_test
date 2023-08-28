from messaging.messengers.messenger_interface import MessengerInterface


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