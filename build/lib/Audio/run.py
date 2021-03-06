from Audio.AudioMain import Audio
from Audio.SyncAlgorithms.correlationSyncNoFilter import correlationSyncNoFilter
from Audio.FingerprintAlgorithms.invariantAlgorithm import invariantAlgorithm
from Audio.database.mongodb_database import mongodb_database
from multiprocessing import Pool
from Audio.QueueWorker.queueWorker import Queueworker
from Audio.Paths import Paths
import threading
import warnings
import time
warnings.filterwarnings("ignore")


# python setup.py sdist bdist_wheel


q = []


def main():
    start_time = time.time()
    audio = Audio(correlationSyncNoFilter(),invariantAlgorithm(),
                  mongodb_database("mongodb://localhost:27017",r'C:\Users\tarun\OneDrive\Desktop\Coding\Audio backend\file.wav'),
                  r'C:\Users\tarun\OneDrive\Desktop\Documents\Music_wav\{}'
                  )
    p = Paths.getInstance()
    p.setRecordingPath(r"C:\Users\tarun\OneDrive\Desktop\Documents\Music_wav\final_file.wav")
    """sync example"""
    audio.sync_audio('Channa Ve (Bhoot).wav',True)



    """Code to fingerprint Songs with following names in /music folder"""

    # import os
    # #
    # Songs = os.listdir(r'C:\Users\tarun\OneDrive\Desktop\Documents\Music_wav')
    # starmap_tuple = []
    # for song in Songs:
    #     starmap_tuple.append(song)
    #     # audio.fingerprint_to_database(song)
    #
    # p2 = Pool()
    # # output = p2.starmap(audio.fingerprint_to_database,starmap_tuple)
    # p2.map(audio.fingerprint_to_database,starmap_tuple)
    # p2.close()
    # p2.join()



    """computing lcs of result obtained"""
    """connencting to database"""
    # result,songs_found = audio.record_result_from_database()
    # print(time.time()-start_time)
    # import pymongo
    # client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
    # db = client['Fingerprints']
    # collection_song = db['SongIds']



    """Using Single Machine multiple cores"""
    # p2 = Pool()
    # data = []
    # for i in range(1,len(result)):
    #     data.append((result[i],result[0]))
    # output = p2.starmap(audio.lcs,data)
    #
    #
    # p2.close()
    # p2.join()
    # SongName = collection_song.find_one({'_id':songs_found[output.index(max(output))]})['SongName']
    # print(SongName)
    # client.close()
    # print("Time taken: " + str(time.time()-start_time))
    # audio.sync_audio(SongName)




    """Using Multiple Machines"""
    # queueWorker = Queueworker(len(result)-1)
    # queueWorker.distribute_load_lcs(2,result)
    # start_time = time.time()
    # t1 = threading.Thread(target=queueWorker.consume, args=(q,))
    # t1.start()
    # t1.join()
    #
    # while(len(q)!=len(result)-1):
    #     pass
    # ma = 0
    # index = -1
    # for i in range(len(q)):
    #     if(ma<q[i][1]):
    #         index = q[i][0]
    #         ma = q[i][1]
    # collection_song = db['SongIds']
    # print(collection_song.find_one({'_id': songs_found[index]}))
    #
    # print(q)
    # print(time.time()-start_time)
    # client.close()
if __name__=='__main__':
    main()
