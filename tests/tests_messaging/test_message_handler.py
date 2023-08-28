import pytest
from unittest.mock import MagicMock
from messaging.message_handling import MessageHandler

class MockMessageInterface:
    def get_type(self):
        pass

    def get_message(self):
        pass

class MockMessengerInterface:
    def send(self, message: str):
        pass

class MockTelegramMessenger(MockMessengerInterface):
    pass

class MockWhatsAppMessenger(MockMessengerInterface):
    pass

def test_handle_success():
    payload = MockMessageInterface()
    payload.get_type = MagicMock(return_value="telegram")
    payload.get_message = MagicMock(return_value="Test message")

    message_handler = MessageHandler()
    message_handler._get_messenger = MagicMock(return_value=MockTelegramMessenger())

    result = message_handler.handle(payload)
    assert result is None  # We assume that a successful handling should return None

def test_handle_exception():
    payload = MockMessageInterface()
    payload.get_type = MagicMock(return_value="unknown")
    payload.get_message = MagicMock(return_value="Test message")

    message_handler = MessageHandler()

    with pytest.raises(ValueError):
        message_handler.handle(payload)