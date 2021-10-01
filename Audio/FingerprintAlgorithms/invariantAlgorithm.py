from Audio.FingerprintAlgorithms.FingerprintAlgorithm import FingerprintAlgorithm
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
from scipy import signal

from Audio.Record.Record import Recorder



class invariantAlgorithm(FingerprintAlgorithm):
    def __init__(self):
        pass

    def fingerprint(self,file_path):
        if(len(file_path)>0):
            data, samplerate = sf.read(file_path)
            if(len(data.shape)>=2):
                data = data[:, 0]
            Pxx, f, t, im = plt.specgram(data, Fs=samplerate, noverlap=500,NFFT=1024,mode='magnitude'
                                         ,cmap='jet')
            # plt.show()
            # f, t, Pxx = signal.spectrogram(data, fs=samplerate,noverlap=120,nfft=2048,mode='magnitude')
            print(Pxx.shape)
            peaks = self.get_peaks(Pxx, f)
            return peaks
        else:
            print("started recording to fingerprint")
            recorder = Recorder(10, 44100, 1, 1)
            data = recorder.record()

            print("stopped recording to fingerprint")
            Pxx, f, t, im = plt.specgram(data, Fs=44100, noverlap=900, NFFT=1024, mode='magnitude'
                                         , cmap='jet')
            peaks = self.get_peaks(Pxx, f)
            return peaks

    def get_peaks(self,Pxx,f):
        peaks = []
        ma=-4000
        ma2 = -4000
        ma3=-4000
        freq3=0
        freq2 = 0
        freq = 0
        for i in range(1,len(Pxx[0])):
            for j in range(20,len(Pxx)):
                if(Pxx[j][i]>ma):
                    ma = Pxx[j][i]
                    freq = f[j]
            for j in range(20,len(Pxx)):
                if(Pxx[j][i]>ma2 and Pxx[j][i]<ma):
                    ma2 = Pxx[j][i]
                    freq2 = f[j]

            if(freq>0 and freq2>0 ):
                temp = [freq,freq2]
                peaks.append(temp)
                ma = -4000
                freq = 0
                ma2 = -4000
                freq2 = 0
                ma3 = -4000
                freq3 = 0
        return peaks

    def print_specgram(self,Pxx,f,t):
         plt.pcolormesh(t, f, Pxx)
         plt.xlabel('Time [sec]')
         plt.colorbar()
         plt.show()

    def lcs(self,X, Y):
        # find the length of the strings
        m = len(X)
        n = len(Y)

        # declaring the array for storing the dp values
        L = [[None] * (n + 1) for i in range(m + 1)]

        """Following steps build L[m + 1][n + 1] in bottom up fashion
        Note: L[i][j] contains length of LCS of X[0..i-1]
        and Y[0..j-1]"""
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        return L[m][n]

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