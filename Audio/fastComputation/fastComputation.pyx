

class fastComputation():
  def __init__(self):
      pass

  def lcs(X,Y):
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

  def get_peaks(Pxx,f):
    peaks = []
    cdef double ma=-4000
    cdef double ma2 = -4000
    cdef double freq2 = 0
    cdef double freq = 0
    for i in range(1,len(Pxx[0])):
        for j in range(20,len(Pxx)): #finding maximum freq
            if(Pxx[j][i]>ma):
                ma = Pxx[j][i]
                freq = f[j]
        for j in range(20,len(Pxx)): #finding second max freq
            if(Pxx[j][i]>ma2 and Pxx[j][i]<ma):
                ma2 = Pxx[j][i]
                freq2 = f[j]
        if(freq>0 and freq2>0):
            temp = [freq,freq2]
            peaks.append(temp)
            ma = -4000
            freq = 0
            ma2 = -4000
            freq2 = 0

    return peaks