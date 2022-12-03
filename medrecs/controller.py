import customtkinter
from customtkinter import BOTH, LEFT, RIGHT, X, Y

from medrecs.model import Model, data_path
from medrecs.entry import Entry
from medrecs.views.home_view import HomeView
from medrecs.views.new_entry_view import NewEntryView
from medrecs.views.entry_list_view import EntryListView


class Controller:
    previous_page = None
    current_page = None

    def __init__(self, model: Model, view: customtkinter.CTkFrame):
        self.model = model
        self.view = view

    def main_page(self):
        for widget in self.view.winfo_children():
            widget.destroy()
        main_page = HomeView(self.view)
        main_page.pack(fill=BOTH, expand=True)
        main_page.set_controller(self)

    def new_entry_page(self):
        for widget in self.view.winfo_children():
            widget.destroy()
        new_entry_page = NewEntryView(self.view, self)
        new_entry_page.pack(fill=BOTH, expand=True)
        new_entry_page.set_controller(self)

    def view_entries_page(self):
        for widget in self.view.winfo_children():
            widget.destroy()
        view_entries_page = EntryListView(self.view, controller=self)
        view_entries_page.pack(fill=BOTH, expand=True)
        view_entries_page.set_controller(self)

    def submit_entry(self, entry: Entry):
        self.model.add_entry(entry)
        self.model.save(data_path)
        self.main_page()

    def get_entry(self, index):
        return self.model.get_entry(index)

    def get_entries(self, start_index=0, end_index=None):
        if not end_index:
            return [self.model.get_entry(i) for i in range(start_index, self.model.get_entry_count())]
        return [self.model.get_entry(i) for i in range(start_index, end_index)]

    def back(self):
        self.main_page()