__author__ = 'Python Object Oriented Programming - A simple notebook application'

import datetime


class Note:
    """
    Define Note...
    """
    last_id = 0

    def __init__(self, memo, tags):
        """
        Initialize the constructor with the data required to create the notebook.
        """
        self.memo = memo
        self.tags = tags

        global last_id
        last_id += last_id
        self.id = last_id
        self.current_date = datetime.datetime.today()

    def match(self, filter):
        """
        Match a string...
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    Create a detailed note book data...
    """
    def __init__(self):
        self.notes = []

    def new_note(self, note, tags):
        self.notes.append(Note(note, tags))

if __name__ == "__main__":
    N1 = Notebook()
    N1.new_note("Hello Tata Elxsi", "Varadarajan")
    print N1.notes