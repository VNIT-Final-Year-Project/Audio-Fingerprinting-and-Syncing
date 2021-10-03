from Audio.AudioMain import Audio
from SyncAlgorithms.correlationSyncNoFilter import correlationSyncNoFilter
from Audio.FingerprintAlgorithms.invariantAlgorithm import invariantAlgorithm
from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    audio = Audio(correlationSyncNoFilter(),invariantAlgorithm())
    # audio.sync_audio()
    Paths = ["",r"C:\Users\tarun\Desktop\music\wolf.wav",
             r"C:\Users\tarun\Desktop\music\stay.wav",
             r"C:\Users\tarun\Desktop\music\chain.wav"]
    # peaks_recorded = audio.fingerprint(file_path="")
    # peaks_song1 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\music\wolf.wav")
    # peak_song2 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\stay.wav")
    # peak_song3 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\music\chain.wav")
    p = Pool()
    result = p.map(audio.fingerprint,Paths)
    for i in range(len(result)):
        print(len(result[i]))
    p.close()
    p.join()
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
    start_time = time.time()
    p2 = Pool()
    data = []
    for i in range(1,len(result)):
        data.append((result[i],result[0]))
    output = p2.starmap(audio.lcs,data)
    # print(audio.lcs(result[1],result[0]))
    # print(audio.lcs(result[2],result[0]))
    # print(audio.lcs(result[3],result[0]))
    print(output)
    print(time.time()-start_time)
    p2.close()
    p2.join()

    # print(audio.fingerprint_algorithm.pattern_match(peaks_song1,peaks_recorded))
    # print(audio.fingerprint_algorithm.pattern_match(peak_song2,peaks_recorded))
    # print(audio.fingerprint_algorithm.pattern_match(peak_song3,peaks_recorded))


