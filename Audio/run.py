from Audio.AudioMain import Audio
from SyncAlgorithms.correlationSyncNoFilter import correlationSyncNoFilter
from Audio.FingerprintAlgorithms.invariantAlgorithm import invariantAlgorithm
from multiprocessing import Pool
from Audio.QueueWorker.queueWorker import Queueworker
import threading

q = []


if __name__ == '__main__':
    audio = Audio(correlationSyncNoFilter(),invariantAlgorithm())
    # audio.sync_audio()
    # peaks_recorded = audio.fingerprint(file_path="")
    Paths = ["",r"C:\Users\tarun\Desktop\music\wolf.wav",
             r"C:\Users\tarun\Desktop\music\stay.wav",
             r"C:\Users\tarun\Desktop\music\chain.wav",
             r"C:\Users\tarun\Desktop\music\wolves.wav",
             r"C:\Users\tarun\Desktop\music\friends2.wav",
             r"C:\Users\tarun\Desktop\music\tu.wav",
             r"C:\Users\tarun\Desktop\music\monster.wav"]

    # peaks_song1 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\music\wolf.wav")
    # peak_song2 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\stay.wav")
    # peak_song3 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\music\chain.wav")
    p = Pool()
    result = p.map(audio.fingerprint,Paths)
    for i in range(len(result)):
        print(len(result[i]))
    p.close()
    p.join()
    # result.insert(0,peaks_recorded)
    # peaks_recorded = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\stay2.wav")

    # fig, axs = plt.subplots(3)
    # fig.suptitle('Vertically stacked subplots')
    # axs[0].plot(peaks_song1)
    # axs[1].plot(peak_song2)
    # axs[2].plot(peaks_recorded)
    # plt.plot(peaks_song1)
    # plt.show()
    # print('length of song1 peaks '+str(len(peaks_song1)))
    # print('length of song2 peaks '+str(len(peak_song2)))
    # print('length of song3 peaks '+str(len(peak_song3)))
    # print(peaks_recorded)

    # print(len(peaks_recorded))
    # print('getting lcs')
    import time
    # start_time = time.time()
    # p2 = Pool()
    # data = []
    # for i in range(1,len(result)):
    #     data.append((result[i],result[0]))
    # output = p2.starmap(audio.lcs,data)
    # # print(audio.lcs(result[1],result[0]))
    # # print(audio.lcs(result[2],result[0]))
    # # print(audio.lcs(result[3],result[0]))
    # print(output)
    # print(time.time()-start_time)
    # p2.close()
    # p2.join()
    queueWorker = Queueworker(len(result)-1)


    for i in range(1,int(len(result)/2)):
        queueWorker.produce(result[i],result[0],i,server='server2')

    for i in range(int(len(result)/2),len(result)):
        queueWorker.produce(result[i],result[0],i,server='server1')
    start_time = time.time()
    t1 = threading.Thread(target=queueWorker.consume, args=(q,))
    t1.start()
    t1.join()


    while(len(q)!=len(result)-1):
        pass
    print(q)
    print(time.time()-start_time)
    # print(audio.fingerprint_algorithm.pattern_match(peaks_song1,peaks_recorded))
    # print(audio.fingerprint_algorithm.pattern_match(peak_song2,peaks_recorded))
    # print(audio.fingerprint_algorithm.pattern_match(peak_song3,peaks_recorded))


