import json


class Write(object):
    def __init__(self):
        pass

    def add_data(self):
        data = \
            {
                'name': 'John',
                'age': 23,
                'username': 'johndoe440',
                'password': 'testing'
            }

        self.dump_data(data)

    def dump_data(self, data):
        print(data)
        with open('test.json', 'w') as file:
            json.dump(data, file)
