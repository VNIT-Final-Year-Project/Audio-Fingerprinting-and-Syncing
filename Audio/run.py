from Audio.AudioMain import Audio
from SyncAlgorithms.correlationSyncNoFilter import correlationSyncNoFilter
from Audio.FingerprintAlgorithms.invariantAlgorithm import invariantAlgorithm
from multiprocessing import Pool
from Audio.QueueWorker.queueWorker import Queueworker
import threading

q = []


if __name__ == '__main__':
    audio = Audio(correlationSyncNoFilter(),invariantAlgorithm())


    # """Code to fingerprint Songs with following names in /music folder"""
    #
    # Songs = ["wolf.wav",
    #          "stay.wav",
    #          "chain.wav",
    #          "wolves.wav",
    #          "friends2.wav",
    #          "tu.wav",
    #          "monster.wav"]
    # starmap_tuple = []
    # for song in Songs:
    #     starmap_tuple.append((song,"mongodb://127.0.0.1:27017"))
    # p2 = Pool()
    # output = p2.starmap(audio.fingerprint_to_database,starmap_tuple)
    # p2.close()
    # p2.join()


    # """computing lcs of result obtained"""
    # result,songs_found = audio.record_result_from_database()
    # import pymongo
    # client = pymongo.MongoClient("mongodb://127.0.0.1:27017", serverSelectionTimeoutMS=5000)
    # db = client['Fingerprints']
    # import time
    # start_time = time.time()
    # p2 = Pool()
    # data = []
    # for i in range(1,len(result)):
    #     data.append((result[i],result[0]))
    # output = p2.starmap(audio.lcs,data)
    # print(output)
    # print(time.time()-start_time)
    # p2.close()
    # p2.join()
    # collection_song = db['SongIds']
    # print(collection_song.find_one({'_id':songs_found[output.index(max(output))]}))


    # queueWorker = Queueworker(len(result)-1)
    #
    # for i in range(1,int(len(result)/2)):
    #     queueWorker.produce(result[i],result[0],i,server='server2')
    #
    # for i in range(int(len(result)/2),len(result)):
    #     queueWorker.produce(result[i],result[0],i,server='server1')
    # start_time = time.time()
    # t1 = threading.Thread(target=queueWorker.consume, args=(q,))
    # t1.start()
    # t1.join()
    #
    # while(len(q)!=len(result)-1):
    #     pass
    # print(q)
    # print(time.time()-start_time)



