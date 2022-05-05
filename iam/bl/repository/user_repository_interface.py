from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def delete(self):
        pass
