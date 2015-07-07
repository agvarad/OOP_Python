__author__ = 'Python Object Oriented Programming - A simple notebook application'

import datetime


class Note:
    """
    Define Note...
    """
    last_id = 0

    def __init__(self, note, tags):
        """
        Initialize the constructor with the data required to create the notebook.
        """
        self.note = note
        self.tags = tags

        global last_id
        last_id += last_id
        self.id = last_id
        self.current_date = datetime.datetime.today()


class Notebook:
    """
    Create a detailed note book data...
    """
    def __init__(self):
        self.notes = []

    def new_note(self, note, tags):
        self.notes.append(Note(note, tags))
