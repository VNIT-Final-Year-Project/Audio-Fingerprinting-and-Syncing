from Audio.Record.Record import Recorder
from Audio.getAudio.getAudio import getAudio
from Audio.SyncAlgorithms.SyncAlgorithm import SyncAlgorithm

import numpy as np
import matplotlib.pyplot as plt


class correlationSyncNoFilter(SyncAlgorithm):
    def __init__(self):
        pass

    def sync(self, file_path):
        recorder = Recorder(5, 44100, 1, 20)
        recording = recorder.record()
        audio = getAudio().get_audio(file_path, 20)
        res_plot = np.correlate(audio, recording, "full")
        plt.plot(res_plot)
        plt.show()
