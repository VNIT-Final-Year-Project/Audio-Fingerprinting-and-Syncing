from Audio.AudioMain import Audio
from SyncAlgorithms.correlationSyncNoFilter import correlationSyncNoFilter

audio = Audio(correlationSyncNoFilter(), "", r"C:\Users\Hp\Desktop\friends2.wav")
audio.sync_audio()
