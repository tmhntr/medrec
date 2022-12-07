import pickle
import os
from uuid import UUID

from medrec.entry import Entry
from medrec.view import PageType
import medrec.database as database


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
    entry_map: dict[str, Entry] = {}
    page_history = []
    current_entry: str

    def __init__(self, path: str = None):
        self.data_path = path

        self.entry_view_model = EntryViewModel(0, 5)

        database.create_db()

    def set_current_entry(self, id: str):
        self.current_entry = id

    def get_current_entry(self) -> Entry:
        return database.get_entry(self.current_entry)

    def add_entry(self, entry: Entry):
        database.add_entry(entry)

    def get_entry(self, id: str):
        return database.get_entry(id)

    def get_entries(self, start_date: str = None, end_date: str = None, entry_type: str = None, limit: int = None, offset: int = None, order_by: str = None):
        return database.get_entries(start_date=start_date, end_date=end_date, entry_type=entry_type, limit=limit, offset=offset, order_by=order_by)

    def get_entry_count(self):
        return database.get_entry_count()

    def remove_entry(self, id: int):
        database.delete_entry(id)

    def set_page(self, page: PageType):
        self.page_history.append(page)

    def get_page(self):
        if len(self.page_history) == 0:
            return PageType.MAIN_PAGE
        return self.page_history[-1]

    def back_page(self):
        self.page_history.pop()
