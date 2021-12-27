import os
import ujson
import uuid


class DataSaver(object):

    def __init__(self):
        self.save_path = os.path.join(os.getcwd(), 'data')
        os.makedirs(self.save_path, exist_ok=True)

    def save_data(self, data):
        file_id = uuid.uuid4()
        with open(os.path.join(self.save_path, '{}.json'.format(file_id)), 'w+', encoding='utf-8') as file:
            for line in data:
                file.write(ujson.dumps(line, ensure_ascii=False))
                file.write('\n')
