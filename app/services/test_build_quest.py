from unittest import TestCase

from models.waypoint import Waypoint
from services.build_campaign import Quest


class TestQuest(TestCase):
    def test__include_waypoint(self):
        quest = Quest()
        waypoint = Waypoint()
