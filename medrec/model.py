import pickle
import os
from uuid import UUID

from medrec.entry import Entry
from medrec.view import PageType

data_path = os.path.join(os.path.dirname(__file__), "../data/entries.pickle")


class EntryViewModel:
    entry_index: int
    display_number: int

    def __init__(self, entry_index: int, display_number: int):
        self.entry_index = entry_index
        self.display_number = display_number

    def set_entry_index(self, entry_index: int):
        self.entry_index = entry_index

    def get_entry_index(self):
        return self.entry_index

    def set_display_number(self, display_number: int):
        self.display_number = display_number

    def get_display_number(self):
        return self.display_number


class Model:
    entries: list[Entry] = []
    entry_map: dict[UUID, Entry] = {}
    page_history = []

    def __init__(self, path: str = None):
        self.data_path = path

        self.entry_view_model = EntryViewModel(0, 5)

        if path is not None:
            self.load(path)

    def add_entry(self, entry: Entry):
        self.entries.append(entry)
        self.entry_map[entry.id] = entry
        self.save()

    def get_entry(self, idx: int):
        if idx < 0 or idx >= len(self.entries):
            return None
        return self.entries[idx]

    def get_entry_by_id(self, id: UUID):
        return self.entry_map[id]

    def get_entries(self):
        return self.entries

    def get_entry_count(self):
        return len(self.entries)

    def remove_entry(self, idx: int):
        del self.entries[idx]
        self.save()

    def remove_all_entries(self):
        self.entries = []
        self.save()

    def save(self):
        # write entries as json to path
        if self.data_path is not None:
            with open(self.data_path, "wb") as f:
                pickle.dump(self.entries, f)
        else:
            raise ValueError("No path specified")

    def load(self, path: str):
        # read entries from json at path
        try:
            with open(path, "rb") as f:
                entries = pickle.load(f)
                for entry in entries:
                    self.entries.append(entry)
                    self.entry_map[entry.id] = entry
                self.entries.sort(key=lambda x: x.date, reverse=True)
        except FileNotFoundError:
            pass

    def set_page(self, page: PageType):
        self.page_history.append(page)

    def get_page(self):
        if len(self.page_history) == 0:
            return PageType.MAIN_PAGE
        return self.page_history[-1]

    def back_page(self):
        self.page_history.pop()
