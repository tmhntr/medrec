from medrec.entry import Entry
from customtkinter import CTkFrame, CTkLabel, CTkTextbox, CTkButton

from medrec.controller import Controller
from medrec.ui.page import Page


class EntryDetailView(Page):
    def __init__(self, parent, controller: Controller = None, entry: Entry = None):
        super().__init__(parent)
        self.set_controller(controller)

        self.header_frame = CTkFrame(self)
        self.header_frame.pack(fill="x", padx=24, pady=20)

        self.back_button = CTkButton(
            self.header_frame, text="Back", command=self.back_button_clicked)
        self.back_button.pack(side="left")

        self.header_label = CTkLabel(self.header_frame, text="Entry Details")
        self.header_label.pack(side="left", fill="x", expand=True)

        self.date_label = CTkLabel(self, text="Date:")
        self.date_label.pack(fill="x")

        self.date_textbox = CTkTextbox(self)
        self.date_textbox.pack(fill="x")

        self.description_label = CTkLabel(self, text="Description:")
        self.description_label.pack(fill="x")

        self.description_textbox = CTkTextbox(self)
        self.description_textbox.pack(fill="x")

        self.entry_type_label = CTkLabel(self, text="Entry Type:")
        self.entry_type_label.pack(fill="x")

        self.entry_type_textbox = CTkTextbox(self)
        self.entry_type_textbox.pack(fill="x")

        self.attachments_label = CTkLabel(self, text="Attachments:")
        self.attachments_label.pack(fill="x")

        self.attachments_textbox = CTkTextbox(self)
        self.attachments_textbox.pack(fill="x")

        self.healthcare_workers_label = CTkLabel(
            self, text="Healthcare Workers:")
        self.healthcare_workers_label.pack(fill="x")

        self.healthcare_workers_textbox = CTkTextbox(self)
        self.healthcare_workers_textbox.pack(fill="x")

        self.medications_label = CTkLabel(self, text="Medications:")
        self.medications_label.pack(fill="x")

        self.medications_textbox = CTkTextbox(self)
        self.medications_textbox.pack(fill="x")

        self.health_data_label = CTkLabel(self, text="Health Data:")
        self.health_data_label.pack(fill="x")

        self.health_data_textbox = CTkTextbox(self)
        self.health_data_textbox.pack(fill="x")

    def set_controller(self, controller: Controller):
        self.controller: Controller = controller

    def back_button_clicked(self):
        if self.controller is not None:
            self.controller.back()

    def update(self, data=None):
        """Update the UI."""
        entry: Entry = data.get("entry")
        if entry is not None:
            self.date_textbox.set_text(entry.date)
            self.description_textbox.set_text(entry.description)
            self.entry_type_textbox.set_text(entry.entry_type)
            self.attachments_textbox.set_text(entry.attachments)
            self.healthcare_workers_textbox.set_text(entry.healthcare_workers)
