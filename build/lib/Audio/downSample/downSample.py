
class downSample:
    def __init__(self):
        pass

    def down_sample(self,data,sample_division_size):
        if(len(data.shape)>1):
            data = data[0::sample_division_size,0]
        else:
            data = data[0::sample_division_size]
        return data