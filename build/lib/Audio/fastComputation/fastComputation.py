
import hashlib
from numba import jit

class fastComputation():
  def __init__(self):
      pass

  def lcs(X, Y):
      m = len(X)
      n = len(Y)

      # allocate storage for one-dimensional lists, `curr` and `prev`
      curr = [0] * (n + 1)
      prev = [0] * (n + 1)

      # fill the lookup table in a bottom-up manner
      for i in range(m + 1):
          for j in range(n + 1):
              if i > 0 and j > 0:
                  # if the current character of `X` and `Y` matches
                  if X[i - 1] == Y[j - 1]:
                      curr[j] = prev[j - 1] + 1
                  # otherwise, if the current character of `X` and `Y` don't match
                  else:
                      curr[j] = max(prev[j], curr[j - 1])

          # replace contents of the previous list with the current list
          prev = curr.copy()

      # LCS will be the last entry in the lookup table
      return curr[n]


  def get_peaks(Pxx,f):
    peaks = []
    ma=-4000
    ma2 = -4000
    freq2 = 0
    freq = 0
    freq3 = 0
    ma3 = -4000
    for i in range(1,len(Pxx[0])):
        for j in range(20,50): #finding maximum freq
            if(Pxx[j][i]>ma):
                ma = Pxx[j][i]
                freq = f[j]
        for j in range(50,80): #finding second max freq
            if(Pxx[j][i]>ma2):
                ma2 = Pxx[j][i]
                freq2 = f[j]

        for j in range(80,110): #finding second max freq
            if(Pxx[j][i]>ma3):
                ma3 = Pxx[j][i]
                freq3 = f[j]

        if(freq>0 and freq2>0 and freq3>0):
            temp = str(freq)+str(freq2)+str(freq3)
            peaks.append(hashlib.md5(temp.encode()).hexdigest())
            ma = -4000
            freq = 0
            ma2 = -4000
            freq2 = 0
            freq3 =0
            ma3=-4000

    return peaks