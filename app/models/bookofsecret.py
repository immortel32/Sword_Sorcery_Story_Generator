from typing import List

from models.chapter import Chapter
from models.event import Event
from models.intruction import Instruction


class BookOfSecret:
    event_table: List[Event] = []
    chapters: List[Chapter] = []

    instruction_setup: List[Instruction] = []

    def append_chapters(self, chapter: Chapter):
        self.chapters.append(chapter)
