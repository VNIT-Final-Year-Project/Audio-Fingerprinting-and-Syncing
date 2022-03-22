from Audio.Record.Record import Recorder
from Audio.getAudio.getAudio import getAudio
from Audio.SyncAlgorithms.SyncAlgorithm import SyncAlgorithm

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time
import sounddevice as sd
import mutagen
from mutagen.wave import WAVE


class correlationSyncNoFilter(SyncAlgorithm):
    def __init__(self):
        pass

    def sync(self, file_path):
        downsampling = 40
        recorder = Recorder(3, 44100, 1, downsampling)
        recording = recorder.record()
        tic = time.perf_counter()
        audio = getAudio().get_audio(file_path, downsampling)
        main_audio = getAudio().get_audio(file_path,1)
        res_plot = signal.correlate(audio, recording, "full")
        id = res_plot.argmax()
        audio_temp = WAVE(file_path)
        ti = audio_temp.info.length
        l = len(main_audio) / ti
        toc = time.perf_counter()
        m = int(downsampling * id + l * (toc - tic))
        y = main_audio[m:]
        sd.play(y)
        time.sleep(10)
        sd.stop()
        print("Sync Time:"+str(toc-tic))
