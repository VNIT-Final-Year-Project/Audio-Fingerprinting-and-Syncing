
import hashlib
import zlib


class fastComputation():
  def __init__(self):
      pass


  def lcs(X, Y):
      m = len(X)
      n = len(Y)

      # declaring the array for storing the dp values
      # L = [[None] * (n + 1) for i in range(m + 1)]
      L = []
      for i in range(m + 1):
          temp = []
          for j in range(n + 1):
              temp.append(0)
          L.append(temp)
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
            # peaks.append(zlib.crc32(temp.encode()))
            # peaks.append(temp)
            ma = -4000
            freq = 0
            ma2 = -4000
            freq2 = 0
            freq3 =0
            ma3=-4000

    return peaks