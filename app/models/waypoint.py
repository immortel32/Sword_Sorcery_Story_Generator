import json
from typing import List
from models.story import Story


class Waypoint:
    title: str = None
    story: List[Story]
    instruction_setup: str = None

    def __init__(self):
        self.stories = []

    def build_from_json(self, json_data: json):
        self.title = json_data["title"]
        if "instruction_setup" in json_data:
            self.instruction_setup = json_data["instruction_setup"]
        for data in json_data["story"]:
            story = Story(data)
            self.stories.append(story)
