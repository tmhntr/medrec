import customtkinter
from customtkinter import BOTH, LEFT, RIGHT, X, Y, CTkEntry, CTkLabel, CTkButton, CTkFrame, BOTTOM

from medrecs.entry import Entry

class NewEntryView(customtkinter.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)

        self.set_controller(controller)

        self.labels = ["Date", "Description", "Entry Type", "Attachments", "Healthcare Workers", "Medications", "Health Data"]
        self.entry_dict = {}
        for i in range(len(self.labels)):
            frame = CTkFrame(self)
            frame.pack(fill=X)

            lbl = CTkLabel(frame, text=self.labels[i])
            lbl.setvar("width", 20)
            lbl.pack(side=LEFT, padx=5, pady=5)

            entry = CTkEntry(frame)
            entry.pack(fill=X, padx=5, expand=True)

            self.entry_dict[self.labels[i]] = entry
        
        submit_button = CTkButton(self, text="Submit", command=self.submit)

        # self.form.pack(fill=customtkinter.BOTH, expand=1, padx=20, pady=40)
        submit_button.pack(side=BOTTOM, expand=True, padx=5, pady=5)


    def set_controller(self, controller):
        self.controller = controller

    def submit(self):
        if self.controller:
            entry = Entry()
            entry.date = self.entry_dict["Date"].get()
            entry.description = self.entry_dict["Description"].get()
            entry.entry_type = self.entry_dict["Entry Type"].get()
            entry.attachments = self.entry_dict["Attachments"].get()
            entry.healthcare_workers = self.entry_dict["Healthcare Workers"].get()
            entry.medications = self.entry_dict["Medications"].get()
            entry.health_data = self.entry_dict["Health Data"].get()

            self.controller.submit_entry(entry)
