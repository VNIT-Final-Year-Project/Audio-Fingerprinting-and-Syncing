from abc import ABC, abstractmethod

class FingerprintAlgorithm(ABC):
    @abstractmethod
    def fingerprint(self):
        pass
