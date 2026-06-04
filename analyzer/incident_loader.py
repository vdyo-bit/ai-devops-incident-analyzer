import json

def load_incident(path):
    with open(path, "r") as file:
        return json.load(file)
