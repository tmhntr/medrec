import customtkinter
from customtkinter import *
from controller import Controller
from view import PageType, View
from ui.page import Page

from entry import Entry

class ViewEntriesGrid(Page):
    def __init__(self, parent):
        super().__init__(parent)
        

        self.update({"entries": []})

    def update(self, data=None):
        """Update the UI."""
        for widget in self.winfo_children():
            widget.destroy()

        entries: list[Entry] = data.get("entries")
        self.grid_columnconfigure(0, weight=1, pad=10)
        self.grid_columnconfigure(1, weight=1, pad=10)
        self.grid_columnconfigure(2, weight=1, pad=10)
        self.grid_columnconfigure(3, weight=1, pad=10)
        self.grid_columnconfigure(4, weight=1, pad=10)
        self.grid_columnconfigure(5, weight=1, pad=10)
        self.grid_columnconfigure(6, weight=1, pad=10)

        for i in range(len(entries) + 1):
            self.grid_rowconfigure(i, weight=1, pad=10)

        self.labels = ["Date", "Description", "Entry Type", "Attachments", "Healthcare Workers", "Medications", "Health Data"]
        for i in range(len(self.labels)):
            label = customtkinter.CTkLabel(self, text=self.labels[i])
            label.grid(row=0, column=i)

        for i in range(len(entries)):
            row = i + 1
            entry = entries[i]
            if entry is not None:
                date = customtkinter.CTkLabel(self, text=entry.date)
                date.grid(row=row, column=0)
                description = customtkinter.CTkLabel(self, text=entry.description)
                description.grid(row=row, column=1)
                entry_type = customtkinter.CTkLabel(self, text=entry.entry_type)
                entry_type.grid(row=row, column=2)
                attachments = customtkinter.CTkLabel(self, text=entry.attachments)
                attachments.grid(row=row, column=3)
                healthcare_workers = customtkinter.CTkLabel(self, text=entry.healthcare_workers)
                healthcare_workers.grid(row=row, column=4)
                medications = customtkinter.CTkLabel(self, text=entry.medications)
                medications.grid(row=row, column=5)
                health_data = customtkinter.CTkLabel(self, text=entry.health_data)
                health_data.grid(row=row, column=6)


class EntryListView(Page):
    def __init__(self, parent, controller: Controller=None):
        super().__init__(parent)

        self.set_controller(controller)

        self.labels = ["Date", "Description", "Entry Type", "Attachments", "Healthcare Workers", "Medications", "Health Data"]

        self.return_button = customtkinter.CTkButton(self, text="Return", command=self.return_to_main)
        self.return_button.pack(side=LEFT)

        self.label = customtkinter.CTkLabel(self, text="View Entries", font=("Arial", 20))
        self.label.pack(fill=X)

        self.table = ViewEntriesGrid(self)
        self.table.pack(fill=BOTH, expand=True)

        self.back_button = customtkinter.CTkButton(self, text="Back", command=self.prev)
        self.back_button.pack()

        self.number_label = customtkinter.CTkLabel(self, text="")
        self.number_label.pack(expand=True)

        self.next_button = customtkinter.CTkButton(self, text="Next", command=self.next)
        self.next_button.pack()

    def return_to_main(self):
        self.controller.set_page(PageType.MAIN_PAGE)

    def update(self, data=None):
        self.table.update(data)
        entries = data.get("entries")
        start_index = data.get("start_index")
        display_count = data.get("display_count")
        entry_count = data.get("entry_count")
        self.number_label.configure(text=f"{start_index + 1} - {min(start_index + display_count, len(entries))} of {len(entries)}")

    def next(self):
        self.controller.elv_next_button_clicked()

    def prev(self):
        self.controller.elv_previous_button_clicked()
