from Audio.FingerprintAlgorithms.FingerprintAlgorithm import FingerprintAlgorithm
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
from scipy import signal
from Audio.fastComputation.fastComputation import fastComputation

from Audio.Record.Record import Recorder
from numba import jit

import ctypes
def malloc_trim():
    ctypes.CDLL('libc.so.6').malloc_trim(0)

class invariantAlgorithm(FingerprintAlgorithm):
    def __init__(self):
        self.lcs = jit()(fastComputation.lcs)
        self.find_peaks = jit()(fastComputation.get_peaks)

    def fingerprint(self,file_path,Record):
        if(Record==False):
            data, samplerate = sf.read(file_path)
            if(len(data.shape)>=2):
                data = data[:, 0]
            Pxx, f, t, im = plt.specgram(data, Fs=samplerate, noverlap=500,NFFT=1024,mode='magnitude'
                                         ,cmap='jet')
            print(Pxx.shape)
            peaks = self.get_peaks(Pxx, f)
            return peaks
        else:
            print("started recording to fingerprint")
            recorder = Recorder(5, 44100, 1, 1)
            data = recorder.record()
            print("stopped recording to fingerprint")
            Pxx, f, t, im = plt.specgram(data, Fs=44100, noverlap=500, NFFT=1024, mode='magnitude'
                                         , cmap='jet')
            peaks = self.get_peaks(Pxx, f)
            return peaks

    def get_peaks(self,Pxx,f):
        return self.find_peaks(Pxx,f)

    def lcs(self,X, Y):
        return self.lcs(X,Y)

    def print_specgram(self,Pxx,f,t):
         plt.pcolormesh(t, f, Pxx)
         plt.xlabel('Time [sec]')
         plt.colorbar()
         plt.show()



    def pattern_match(self,X,Y):
        n = len(X)
        m = len(Y)
        ans = 0
        for i in range(n-m+1):
            temp_ans = 0
            for j in range(m):
                if(X[i+j]==Y[j]):
                    temp_ans = temp_ans+1
            ans = max(ans,temp_ans)
        return ans