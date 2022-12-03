import customtkinter
from customtkinter import *

from medrecs.entry import Entry

class ViewEntriesGrid(customtkinter.CTkFrame):
    def __init__(self, parent, entries: list[Entry], controller=None):
        super().__init__(parent)
        

        self.update(entries)

    def update(self, entries: list[Entry]):
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

    def set_controller(self, controller):
        self.controller = controller

class EntryListView(customtkinter.CTkFrame):
    start_index = 0
    display_count = 5

    entries = []

    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.set_controller(controller)

        self.get_entries()

        self.labels = ["Date", "Description", "Entry Type", "Attachments", "Healthcare Workers", "Medications", "Health Data"]

        self.return_button = customtkinter.CTkButton(self, text="Return", command=self.controller.main_page)
        self.return_button.pack(side=LEFT)

        self.label = customtkinter.CTkLabel(self, text="View Entries", font=("Arial", 20))
        self.label.pack(fill=X)

        self.table = ViewEntriesGrid(self, self.entries[self.start_index:self.start_index + self.display_count])
        self.table.pack(fill=BOTH, expand=True)

        self.back_button = customtkinter.CTkButton(self, text="Back", command=self.back)
        self.back_button.pack()

        self.number_label = customtkinter.CTkLabel(self, text=f"{self.start_index + 1} - {min(self.start_index + self.display_count, len(self.entries))} of {len(self.entries)}")
        self.number_label.pack(expand=True)

        self.next_button = customtkinter.CTkButton(self, text="Next", command=self.next)
        self.next_button.pack()


    def set_controller(self, controller):
        self.controller = controller

    def get_entries(self):
        if self.controller:
            self.entries = self.controller.get_entries()

    def set_display_count(self, count):
        self.display_count = count
        self.table.display_count = count

    def update(self):
        self.get_entries()
        self.table.destroy()

        self.table.update()
        self.number_label.config(text=f"{self.start_index + 1} - {self.start_index + self.display_count} of {len(self.entries)}")

    def next(self):
        self.start_index += self.display_count
        self.update()

    def back(self):
        self.start_index -= self.display_count
        self.update()
