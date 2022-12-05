from customtkinter import BOTH, LEFT, RIGHT, X, Y, CTkEntry, CTkLabel, CTkButton, CTkFrame, BOTTOM
from controller import Controller
from ui.page import Page

class NewEntryView(Page):
    def __init__(self, parent, controller: Controller=None):
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

            self.entry_dict[self.labels[i].lower().replace(" ", "_")] = entry
        
        submit_button = CTkButton(self, text="Submit", command=self.submit)

        # self.form.pack(fill=customtkinter.BOTH, expand=1, padx=20, pady=40)
        submit_button.pack(side=BOTTOM, expand=True, padx=5, pady=5)


    def set_controller(self, controller: Controller):
        self.controller = controller

    def submit(self):
        if self.controller:
            entry_data = {}
            for key, entry in self.entry_dict.items():
                entry_data[key] = entry.get()
            self.controller.nev_submit_entry(entry_data)

    def update(self, data=None):
        pass
