from dataclasses import dataclass

@dataclass
class Paths:
    instance = -1
    recordingPath = ''

    @staticmethod
    def getInstance():
        if(Paths.instance!=-1):
            return Paths.instance
        else:
            Paths.instance = Paths()
            return Paths.instance

    def __init__(self):
        pass

    def setRecordingPath(self,recordingPath):
        self.instance.recordingPath = recordingPath
