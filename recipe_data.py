import json

def load_recipes():
    with open("data.json", "r") as file:
        return json.load(file)
