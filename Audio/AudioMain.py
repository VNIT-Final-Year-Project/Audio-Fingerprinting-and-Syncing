class Audio:

    def __init__(self, sync_algorithm, fingerprint_algorithm, file_path):
        self.sync_algorithm = sync_algorithm
        self.fingerprint_algorithm = fingerprint_algorithm
        self.file_path = file_path

    def sync_audio(self):
        self.sync_algorithm.sync(self.file_path)

    def find_audio(self):
        self.fingerprint_algorithm.find()
