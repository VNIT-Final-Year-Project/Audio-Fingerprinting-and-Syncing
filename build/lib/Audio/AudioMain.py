import pymongo
import collections
import time

class Audio:

    def __init__(self, sync_algorithm, fingerprint_algorithm, database):
        self.sync_algorithm = sync_algorithm
        self.fingerprint_algorithm = fingerprint_algorithm
        self.database = database
        self.base_path = r'/home/tarundecipher/Documents/Music_wav/{}'


    def sync_audio(self,SongName):
        self.sync_algorithm.sync(self.base_path.format(SongName))

    def fingerprint(self,SongName,Record):
        return self.fingerprint_algorithm.fingerprint(self.base_path.format(SongName),Record)

    def fingerprint_to_database(self,SongName):
        self.database.fingerprint_to_database(SongName,self)

    def record_result_from_database(self):
        return self.database.record_result_from_database(self)

    def lcs(self,list1,list2):
       return  self.fingerprint_algorithm.lcs(list1,list2)