# Modules
import json

# Main
PERSONS_PATH = "../db/persons.json"

class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def load_persons_data():
        with open(PERSONS_PATH, "r") as file:
            data = json.load(file)
            file.close()

        return data