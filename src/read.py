import json


class Read(object):
    def __init__(self):
        pass

    def read_data(self):
        with open('test.json', 'r') as file:
            data = json.load(file)

            return data
