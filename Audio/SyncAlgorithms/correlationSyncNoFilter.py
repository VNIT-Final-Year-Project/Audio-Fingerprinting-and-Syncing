from Audio.Record.Record import Recorder
from Audio.getAudio.getAudio import getAudio
from Audio.SyncAlgorithms.SyncAlgorithm import SyncAlgorithm
from Audio.Paths import Paths

from scipy import signal
import time
import sounddevice as sd
from mutagen.wave import WAVE


class correlationSyncNoFilter(SyncAlgorithm):
    def __init__(self):
        pass

    def sync(self, file_path,recordit):
        if(recordit):
            downsampling = 20
            recorder = Recorder(3, 44100, 1, downsampling)
            recording = recorder.record()
            tic = time.time()
            audio = getAudio().get_audio(file_path, downsampling)
            main_audio = getAudio().get_audio(file_path,1)
            res_plot = signal.correlate(audio, recording, "full")
            id = res_plot.argmax()
            audio_temp = WAVE(file_path)
            ti = audio_temp.info.length
            l = len(main_audio) / ti
            toc = time.time()
            m = int(downsampling * id + l * (toc - tic))
            y = main_audio[m:]
            sd.play(y)
            time.sleep(10)
            sd.stop()
            print("Sync Time:"+str(toc-tic))
        else:
            downsampling = 20
            obj = Paths.getInstance()
            file_path_recording = obj.recordingPath
            recording = getAudio().get_audio(file_path_recording, downsampling)
            tic = time.time()
            audio = getAudio().get_audio(file_path, downsampling)
            main_audio = getAudio().get_audio(file_path, 1)
            res_plot = signal.correlate(audio, recording, "full")
            id = res_plot.argmax()
            audio_temp = WAVE(file_path)
            ti = audio_temp.info.length
            l = len(main_audio) / ti
            originalSyncPoint = downsampling*id
            originalSyncduration = originalSyncPoint/l
            toc = time.time()
            print(toc-tic+originalSyncduration)
            print((toc-tic+originalSyncduration)-60)




