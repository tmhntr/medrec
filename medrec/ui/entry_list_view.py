import customtkinter
from customtkinter import *
from medrec.controller import Controller
from medrec.ui.header import Header
from medrec.view import PageType, View
from medrec.ui.page import Page

from medrec.entry import Entry


class ViewEntriesGrid(Page):
    entries: list[Entry] = []
    labels = ["Date", "Description", "Entry Type"]

    def __init__(self, parent, entries: list[Entry] = [], controller: Controller = None):
        super().__init__(parent)

        self.update(entries)

    def update(self, entries: list[Entry] = []):
        """Update the UI."""
        for widget in self.winfo_children():
            widget.destroy()

        self.entries = entries
        self.grid_columnconfigure(0, weight=1, pad=10)
        self.grid_columnconfigure(1, weight=1, pad=10)
        self.grid_columnconfigure(2, weight=1, pad=10)
        self.grid_columnconfigure(3, weight=1, pad=10)

        for i in range(len(self.entries) + 1):
            self.grid_rowconfigure(i, weight=1, pad=10)

        for i, label in enumerate(self.labels):
            label = customtkinter.CTkLabel(self, text=label)
            label.grid(row=0, column=i)

        for i, entry in enumerate(self.entries):
            row = i + 1
            if entry is not None:
                date = customtkinter.CTkLabel(self, text=entry.date)
                date.grid(row=row, column=0)
                description = customtkinter.CTkLabel(
                    self, text=entry.description)
                description.grid(row=row, column=1)
                entry_type = customtkinter.CTkLabel(
                    self, text=entry.entry_type)
                entry_type.grid(row=row, column=2)

                edit_button = customtkinter.CTkButton(
                    self, text="Edit", command=lambda: self.edit_entry_clicked(entry.id))
                edit_button.grid(row=row, column=3)

    def edit_entry_clicked(self, entry_id):
        if self.controller:
            self.controller.edit_entry(entry_id)


class EntryListView(Page):
    entries: list[Entry] = []
    start_index: int = 0
    display_count: int = 10
    entry_count: int = 0

    def __init__(self, parent, controller: Controller = None, entries: list[Entry] = None, start_index: int = None, display_count: int = None, entry_count: int = None):
        super().__init__(parent)

        self.set_controller(controller)

        self.header = Header(self, label="View Entries",
                             controller=self.controller, has_back_button=True)
        self.header.pack(fill=X, expand=True, padx=24, pady=20)

        self.table = ViewEntriesGrid(self)
        self.table.pack(fill=BOTH, expand=True, padx=24, pady=20)

        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.pack(side=BOTTOM, expand=True, padx=24, pady=20)

        self.back_button = customtkinter.CTkButton(
            self.button_frame, text="Back", command=self.prev)
        self.back_button.pack(side=LEFT, padx=12, pady=10)

        self.number_label = customtkinter.CTkLabel(self.button_frame, text="")
        self.number_label.pack(side=LEFT, padx=12, pady=10)

        self.next_button = customtkinter.CTkButton(
            self.button_frame, text="Next", command=self.next)
        self.next_button.pack(side=LEFT, padx=12, pady=10)

        self.update(entries=entries, start_index=start_index,
                    display_count=display_count, entry_count=entry_count)

    def return_to_main(self):
        self.controller.set_page(PageType.MAIN_PAGE)

    def update(self, entries: list[Entry] = None, start_index: int = None, display_count: int = None, entry_count: int = None):
        if self.entries is not None:
            self.table.update(entries=entries)
            self.entries = entries
        if entry_count is not None:
            self.entry_count = entry_count
        if display_count is not None:
            self.display_count = display_count
        if start_index is not None:
            self.start_index = start_index

        self.number_label.configure(
            text=f"{self.start_index + 1} - {min(self.start_index + self.display_count, self.entry_count)} of {self.entry_count}")

    def next(self):
        self.controller.elv_next_button_clicked()

    def prev(self):
        self.controller.elv_previous_button_clicked()
