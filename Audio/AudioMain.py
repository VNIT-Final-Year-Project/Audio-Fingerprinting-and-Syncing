class Audio:

    def __init__(self, sync_algorithm, fingerprint_algorithm):
        self.sync_algorithm = sync_algorithm
        self.fingerprint_algorithm = fingerprint_algorithm


    def sync_audio(self,file_path):
        self.sync_algorithm.sync(file_path)

    def fingerprint(self,file_path):
        return self.fingerprint_algorithm.fingerprint(file_path)

    def lcs(self,list1,list2):
       return  self.fingerprint_algorithm.lcs(list1,list2)