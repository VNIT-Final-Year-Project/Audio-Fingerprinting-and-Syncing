from Audio.Record.Record import Recorder
import sounddevice as sd
from skimage.restoration import denoise_wavelet
import numpy as np

#with noise
recorder = Recorder(10, 44100, 1, 1)
recording =  recorder.record()
sd.play(recording)
sd.wait()

#after removing noise
recording_denoise = denoise_wavelet(recording,method = 'BayesShrink',mode ='soft',wavelet_levels=8
                ,wavelet='haar',rescale_sigma=True)

sd.play(recording_denoise)
sd.wait()

recording_difference = recording - recording_denoise
sd.play(recording_difference)
sd.wait()