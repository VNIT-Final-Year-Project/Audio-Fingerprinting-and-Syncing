import soundfile as sf
from Audio.downSample.downSample import downSample

class getAudio:
    def __init__(self):
        pass

    def get_audio(self, file_path, sample_division_size):
        data, samplerate = sf.read(file_path)
        data = downSample().down_sample(data,sample_division_size)
        return data