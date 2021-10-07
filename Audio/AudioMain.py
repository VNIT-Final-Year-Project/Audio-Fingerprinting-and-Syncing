class Audio:

    def __init__(self, sync_algorithm, fingerprint_algorithm):
        self.sync_algorithm = sync_algorithm
        self.fingerprint_algorithm = fingerprint_algorithm
        self.base_path = r'C:\Users\tarun\Desktop\music\{}'


    def sync_audio(self,SongName):
        self.sync_algorithm.sync(self.base_path.format(SongName))

    def fingerprint(self,SongName,Record):
        return self.fingerprint_algorithm.fingerprint(self.base_path.format(SongName),Record)

    def fingerprint_to_database(self,SongName,connection_string):
        peaks = self.fingerprint(SongName,False)
        import pymongo
        client = pymongo.MongoClient(connection_string,serverSelectionTimeoutMS=5000)
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

    def record_result_from_database(self):
        """Code to retrieve data of recorded song match from database"""
        import pymongo
        import collections

        dict = collections.defaultdict(list)
        songs_found = []
        client = pymongo.MongoClient("mongodb://127.0.0.1:27017", serverSelectionTimeoutMS=5000)
        db = client['Fingerprints']
        collections_hash = db['HashValues']
        peaks = self.fingerprint("", True)
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
        return result,songs_found

    def lcs(self,list1,list2):
       return  self.fingerprint_algorithm.lcs(list1,list2)