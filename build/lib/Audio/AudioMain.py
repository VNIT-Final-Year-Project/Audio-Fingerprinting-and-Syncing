import pymongo
import collections
import time

class Audio:

    def __init__(self, sync_algorithm, fingerprint_algorithm, database,base_path):
        self.sync_algorithm = sync_algorithm
        self.fingerprint_algorithm = fingerprint_algorithm
        self.database = database
        self.base_path = base_path

    """This syncs the base_path + songName provided with the recorded snippet"""
    def sync_audio(self,SongName):
        self.sync_algorithm.sync(self.base_path.format(SongName))

    """This function returns the list of peaks for a SongName provided if Record is false.
    If Record is set True then it will return peaks for the recorded audio"""
    def fingerprint(self,SongName,Record):
        return self.fingerprint_algorithm.fingerprint(self.base_path.format(SongName),Record)

    """This function writes fingerprint to database of the base_path+SongName provided"""
    def fingerprint_to_database(self,SongName):
        self.database.fingerprint_to_database(SongName,self)

    """This function returns result,songs_found for the recorded snippet from the database
    result contains a 2D list [[],[]..] of peaks where result[0] is peak for the recorded 
    audio which need to be matched with other record indices like record[1],record[2].
    songs_found contains the id of the songs found from the database where record[1]
    corresponds to songs_found[0] because record[0] is for recorded audio."""
    def record_result_from_database(self):
        return self.database.record_result_from_database(self)

    def result_from_database(self):
        return self.database.result_from_database(self)


    """This function is used to return the LCS value for the two lists provided as arguements.
    These lists will be list of peak values coming from the fingerprint function."""
    def lcs(self,list1,list2):
       return  self.fingerprint_algorithm.lcs(list1,list2)