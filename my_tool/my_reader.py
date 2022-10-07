# from pprint import pprint #for debug

class LoadSetting(object):
    """docstring forLoadSetting."""
    def __init__(self, file_dir):
        super(LoadSetting, self).__init__()
        self.file_dir = file_dir

    def load_as_text(self):
        read_as_text = open(self.file_dir, "r").read()
        # pprint(read_as_text) #for debug
        return read_as_text

    def load_as_json(self):
        read_as_text = open(self.file_dir, "r").read()
        load_as_json = json.loads(read_as_text)
        # pprint(load_as_json) #for debug
        return load_as_json