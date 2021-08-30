
class downSample:
    def __init__(self):
        pass

    def down_sample(self,data,sample_division_size):
        data = data[0::sample_division_size,0]
        return data