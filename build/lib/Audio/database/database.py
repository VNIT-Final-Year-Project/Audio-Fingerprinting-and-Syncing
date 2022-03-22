from abc import ABC, abstractmethod

class database(ABC):
    @abstractmethod
    def fingerprint_to_database(self,SongName):
        pass
    def record_result_from_database(self):
        pass
