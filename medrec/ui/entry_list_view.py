import customtkinter
from customtkinter import *
from medrec.controller import Controller
from medrec.view import PageType, View
from medrec.ui.page import Page

from medrec.entry import Entry


class ViewEntriesGrid(Page):
    entries: list[Entry] = []

    def __init__(self, parent):
        super().__init__(parent)

        self.update({"entries": []})

    def update(self, data=None):
        """Update the UI."""
        for widget in self.winfo_children():
            widget.destroy()

        self.entries: list[Entry] = data.get("entries")
        self.grid_columnconfigure(0, weight=1, pad=10)
        self.grid_columnconfigure(1, weight=1, pad=10)
        self.grid_columnconfigure(2, weight=1, pad=10)
        self.grid_columnconfigure(3, weight=1, pad=10)

        for i in range(len(self.entries) + 1):
            self.grid_rowconfigure(i, weight=1, pad=10)

        self.labels = ["Date", "Description", "Entry Type"]
        for i in range(len(self.labels)):
            label = customtkinter.CTkLabel(self, text=self.labels[i])
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
    def __init__(self, parent, controller: Controller = None):
        super().__init__(parent)

        self.set_controller(controller)

        self.header_frame = customtkinter.CTkFrame(self)
        self.header_frame.pack(side=TOP, fill=X)

        self.return_button = customtkinter.CTkButton(
            self.header_frame, text="Return", command=self.return_to_main)
        self.return_button.pack(side=LEFT, padx=24, pady=20)

        self.label = customtkinter.CTkLabel(
            self.header_frame, text="View Entries", font=("Arial", 20))
        self.label.pack(fill=X, expand=True, padx=24, pady=20)

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

    def return_to_main(self):
        self.controller.set_page(PageType.MAIN_PAGE)

    def update(self, data=None):
        self.table.update(data)
        entries = data.get("entries")
        start_index = data.get("start_index")
        display_count = data.get("display_count")
        entry_count = data.get("entry_count")
        self.number_label.configure(
            text=f"{start_index + 1} - {min(start_index + display_count, len(entries))} of {len(entries)}")

    def next(self):
        self.controller.elv_next_button_clicked()

    def prev(self):
        self.controller.elv_previous_button_clicked()
