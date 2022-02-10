from Audio.database.database import database
import pymongo
import collections
import ctypes
def malloc_trim():
    ctypes.CDLL('libc.so.6').malloc_trim(0)

class mongodb_database(database):
    def __init__(self,connection_string):
        self.connection_string = connection_string


    def fingerprint_to_database(self, SongName,Audio):
        peaks = Audio.fingerprint(SongName,False)
        client = pymongo.MongoClient(self.connection_string,serverSelectionTimeoutMS=5000)
        try:
            print(client.server_info())
            db = client['Fingerprints']
            collection_ids = db['SongIds']
            result = collection_ids.find_one({'SongName':SongName})
            songId = ""
            if(result==None):
                collection_ids.insert({'SongName':SongName})
                result = collection_ids.find_one({'SongName': SongName})
                songId = result['_id']
                collection_hash = db['HashValues']
                for i in range(len(peaks)):
                    collection_hash.update({"hash": peaks[i]}, {'$push': {'Values': [songId, i]}}, True)
            print(SongName+" fingerprinted")
            del peaks
            del collection_hash
            del collection_ids
            del result
            client.close()
        except Exception as e:
            print(e)
        malloc_trim()

    def record_result_from_database(self,Audio):
        """Code to retrieve data of recorded song match from database"""

        dict = collections.defaultdict(list)
        songs_found = []
        client = pymongo.MongoClient(self.connection_string,serverSelectionTimeoutMS=5000)
        db = client['Fingerprints']
        collections_hash = db['HashValues']
        peaks = Audio.fingerprint("", True)
        for peak in peaks:
            array = collections_hash.find_one({'hash': peak})
            if (array != None):
                array = array['Values']
                for element in array:
                    dict[element[0]].append([element[1], peak])
                    songs_found.append(element[0])
        songs_found = set(songs_found)
        songs_found = (list(songs_found))
        result = [peaks]
        for song in songs_found:
            dict[song].sort()
            temp = []
            for element in dict[song]:
                temp.append(element[1])
            result.append(temp)
        client.close()
        return result, songs_found
