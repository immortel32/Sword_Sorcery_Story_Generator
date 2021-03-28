from typing import List

from models.book_of_secret import Book_Of_Secret
from models.chapter import Chapter
from models.event import Event
from models.intruction import Instruction
from models.waypoint import Waypoint
from log_setup import log


class Quest:
    book_of_secret = Book_Of_Secret()
    quest_number = 1
    chapter_number = 1

    # -----------------------------------------
    def _get_chapter_index(self) -> str:
        index = f"{self.quest_number}.{self.chapter_number}"
        self.chapter_number = self.chapter_number + 1
        return index

    # -----------------------------------------

    def _include_waypoint(self, waypoint: Waypoint, event_name: str):
        log.info(f"Method = _include_waypoint {waypoint.title}, contains {len(waypoint.stories)} stories")
        chapter_index = {}

        # Generating the chapter number for all indexes of the sub-story
        for i in range(0, len(waypoint.stories)):
            # Pre-Generate the chapter index for each story
            index = self._get_chapter_index()
            log.info(f"   Generating index {i + 1} = {index}")
            chapter_index[f"INDEX_{i + 1}"] = index

        # Adding chapters to the book of secret
        for story in waypoint.stories:
            chapter = Chapter()
            chapter.id = chapter_index[f"INDEX_{story.index}"]
            chapter.title = waypoint.title
            chapter.text = story.text
            while chapter.text.find("<<INDEX") != -1:
                replace_index = chapter.text[(chapter.text.find("<<INDEX") + 2):chapter.text.find(">>")]
                log.info(f"replace_index = {replace_index}")
                chapter.text = chapter.text.replace(f"<<{replace_index}>>", chapter_index[replace_index])
            self.book_of_secret.append_chapters(chapter)

        # Create and add Event to book of secret
        event = Event()
        event.name = event_name
        event.reference = chapter_index["INDEX_1"]
        self.book_of_secret.event_table.append(event)

        # Creating instructions
        if waypoint.instruction_setup:
            instruction = Instruction()
            instruction.source = event_name
            instruction.instruction = waypoint.instruction_setup
            self.book_of_secret.instruction_setup.append(instruction)

    # -----------------------------------------

    def build_quest(self, waypoint_list: List[Waypoint]):

        i = 1
        for waypoint in waypoint_list:
            event_name = f"Point de cheminement {i}"
            i = i + 1
            self._include_waypoint(waypoint, event_name)

        print("Livre des contes")
        print(f"--------------------")
        print(f"--------------------")
        print(f"Instructions de mise en place")
        for instruction in self.book_of_secret.instruction_setup:
            print(f"   - {instruction.source} = {instruction.instruction}")
        print(f"---")
        print(f" ")
        print(f"Table des événements")
        for event in self.book_of_secret.event_table:
            print(f"   - {event.name} = {event.reference}")
        print(f"---")


        print(f"--------------------")
        print(f" ")
        print(f" ")

        print("Livre des secrets")
        print(f"--------------------")
        print(f"--------------------")
        print(f" ")
        for chapter in self.book_of_secret.chapters:
            print(f"{chapter.id} - {chapter.title}")
            print(f"")
            print(f"{chapter.text}")
            print(f"---")
            print(f" ")
