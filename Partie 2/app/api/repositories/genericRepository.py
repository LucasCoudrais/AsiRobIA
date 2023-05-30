import json

class GenericRepository:
    def __init__(self, filename):
        self.filename = filename

    def read_entity(self):
        with open(self.filename, 'r') as file:
            entities = json.load(file)
        return entities

    def write_entity(self, entities):
        with open(self.filename, 'w') as file:
            json.dump(entities, file)
