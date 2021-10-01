from Audio.AudioMain import Audio
from SyncAlgorithms.correlationSyncNoFilter import correlationSyncNoFilter
from Audio.FingerprintAlgorithms.invariantAlgorithm import invariantAlgorithm
import matplotlib.pyplot as plt
import numpy as np


audio = Audio(correlationSyncNoFilter(),invariantAlgorithm())
# audio.sync_audio()
peaks_recorded = audio.fingerprint(file_path="")
peaks_song1 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\music\wolf.wav")
peak_song2 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\stay.wav")
peak_song3 = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\music\chain.wav")
# peaks_recorded = audio.fingerprint(file_path=r"C:\Users\tarun\Desktop\stay2.wav")

# fig, axs = plt.subplots(3)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(peaks_song1)
# axs[1].plot(peak_song2)
# axs[2].plot(peaks_recorded)

# plt.plot(peaks_song1)
# plt.show()
print('length of song1 peaks '+str(len(peaks_song1)))
print('length of song2 peaks '+str(len(peak_song2)))
print('length of song3 peaks '+str(len(peak_song3)))
# print(peaks_recorded)

# print(len(peaks_recorded))
print('getting lcs')
print(audio.lcs(peaks_song1,peaks_recorded))
print(audio.lcs(peak_song2,peaks_recorded))
print(audio.lcs(peak_song3,peaks_recorded))
# print(audio.fingerprint_algorithm.pattern_match(peaks_song1,peaks_recorded))
# print(audio.fingerprint_algorithm.pattern_match(peak_song2,peaks_recorded))
# print(audio.fingerprint_algorithm.pattern_match(peak_song3,peaks_recorded))


