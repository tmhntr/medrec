import pickle
import os

from medrecs.entry import Entry

data_path = os.path.join(os.path.dirname(__file__), "../data/entries.pickle")


class Model:
    def __init__(self, path: str = None):
        self.entries = []
        if path is not None:
            self.load(path)

    def add_entry(self, entry: Entry):
        self.entries.append(entry)

    def get_entry(self, idx: int):
        return self.entries[idx]

    def get_entries(self):
        return self.entries

    def get_entry_count(self):
        return len(self.entries)

    def remove_entry(self, idx: int):
        del self.entries[idx]

    def remove_all_entries(self):
        self.entries = []

    def save(self, path: str):
        # write entries as json to path
        with open(path, "wb") as f:
            pickle.dump(self.entries, f)

    def load(self, path: str):
        # read entries from json at path
        try:
            with open(path, "rb") as f:
                self.entries = pickle.load(f)
        except FileNotFoundError:
            pass