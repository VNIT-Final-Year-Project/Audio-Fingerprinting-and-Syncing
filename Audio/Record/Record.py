import sounddevice as sd


class Recorder:
    def __init__(self, duration, sampling_freq, sound_device_id, sample_division_size):
        self.duration = duration
        self.sampling_freq = sampling_freq
        self.sound_device_id = sound_device_id
        self.sample_division_size = sample_division_size

    def record(self):
        recording = sd.rec(int(self.duration * self.sampling_freq), samplerate=self.sampling_freq, channels=1)
        sd.wait()
        recording = recording[0::self.sample_division_size, 0]
        return recording
