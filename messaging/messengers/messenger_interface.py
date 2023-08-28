from abc import ABC, abstractmethod


class MessengerInterface(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass