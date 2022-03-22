from Audio.database.database import database
import pymongo
import collections


class mongodb_database(database):
    def __init__(self,connection_string,recordedFilePath):
        self.connection_string = connection_string
        self.recordedFilePath = recordedFilePath


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

            client.close()
        except Exception as e:
            print(e)


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

    def result_from_database(self,Audio):
        """Code to retrieve data of recorded song match from database"""

        dict = collections.defaultdict(list)
        songs_found = []
        client = pymongo.MongoClient(self.connection_string,serverSelectionTimeoutMS=5000)
        db = client['Fingerprints']
        collections_hash = db['HashValues']
        peaks = Audio.fingerprint(self.recordedFilePath, False)
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
