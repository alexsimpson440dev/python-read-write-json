import json


class Write(object):
    def __init__(self):
        pass

    def add_data(self, name, age, username, password):
        data = \
            {
                'name': name,
                'age': age,
                'username': username,
                'password': password
            }

        self.dump_data(data)

    def dump_data(self, data):
        with open('test.json', 'w') as file:
            json.dump(data, file)
