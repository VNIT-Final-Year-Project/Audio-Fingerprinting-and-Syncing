import io
import soundfile as sf
from urllib.request import urlopen

# url = "https://rr11---sn-ci5gup-qxa6.googlevideo.com/videoplayback?expire=1643909214&ei=_rv7YeaWDZK14-EPrPeV6Aw&ip=122.161.75.101&id=o-AANkH3MNJTTU6oG6iR3mmIl-wASJFfTgWmCLwbVrFvnV&itag=140&source=youtube&requiressl=yes&mh=d0&mm=31%2C26&mn=sn-ci5gup-qxa6%2Csn-cvh76nez&ms=au%2Conr&mv=m&mvi=11&pcm2cms=yes&pl=22&initcwndbps=1035000&vprv=1&mime=audio%2Fmp4&ns=sYP1Co-HCWYMWD10IyEKPQwG&gir=yes&clen=3547604&dur=219.149&lmt=1630763349217843&mt=1643887257&fvip=5&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5432434&n=SqcAWENjbSBFS4B&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAORCbZ_9vbLS1_wioIM2a5A_6Cbf679hXNVWieAdeE0UAiEAoKEzgCoNWIKTuDqFARl7VfZkWqNwH3WmXfnhQ0avu8Y%3D&sig=AOq0QJ8wRAIgF6_X8ctIli5mbAbC0NXw-lVXoLprvIND7x2y3XVFnzsCIBqj0GOBXvsVR5m4rDV622JkMSqBk3wTB5QaYaDWdjvi"
path = "/home/tarundecipher/Downloads/videoplayback.wav"
# data, samplerate = sf.read(io.BytesIO(urlopen(url).read()))
data,samplerate = sf.read(path)
print(data,samplerate)