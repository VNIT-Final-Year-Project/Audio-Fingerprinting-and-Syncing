from abc import ABC, abstractmethod

class SyncAlgorithm(ABC):
    @abstractmethod
    def sync(self):
        pass
