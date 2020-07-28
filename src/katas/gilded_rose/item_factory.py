from abc import ABC, abstractmethod


class AbstractItem(ABC):

    @abstractmethod
    def tick(self):
        pass
