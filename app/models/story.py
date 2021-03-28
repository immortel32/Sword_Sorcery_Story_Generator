import json


class Story:
    index: int
    text: str

    def __init__(self, json_data:json):
        self.index = json_data["index"]
        self.text = json_data["text"]
