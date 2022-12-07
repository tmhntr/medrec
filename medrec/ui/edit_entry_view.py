from customtkinter import BOTH, LEFT, RIGHT, TOP, X, Y, CTkEntry, CTkLabel, CTkButton, CTkFrame, BOTTOM, CTkComboBox
from medrec.controller import Controller
from medrec.ui.page import Page
from medrec.entry import Entry, EntryType, MedicationEntry


class MedicationEntryForm(CTkFrame):
    def __init__(self, parent, controller: Controller = None, entry: MedicationEntry = None):
        super().__init__(parent)

        self.controller = controller
        self.entry = entry if entry else MedicationEntry()

        self.grid_columnconfigure(0, pad=10)
        self.grid_columnconfigure(1, pad=10, weight=1)

        self.grid_rowconfigure(0, pad=10)
        self.grid_rowconfigure(1, pad=10)
        self.grid_rowconfigure(2, pad=10)
        self.grid_rowconfigure(3, pad=10)
        self.grid_rowconfigure(4, pad=10)
        self.grid_rowconfigure(5, pad=10)
        self.grid_rowconfigure(6, pad=10)
        self.grid_rowconfigure(7, pad=10)

        self.date_label = CTkLabel(self, text="Date")
        self.date_label.grid(row=0, column=0, sticky="w")

        self.date_entry = CTkEntry(self)
        self.date_entry.grid(row=0, column=1, sticky="w")

        self.name_label = CTkLabel(self, text="Name")
        self.name_label.grid(row=1, column=0, sticky="w")

        self.name_entry = CTkEntry(self)
        self.name_entry.grid(row=1, column=1, sticky="w")

        self.dosage_label = CTkLabel(self, text="Dosage")
        self.dosage_label.grid(row=2, column=0, sticky="w")

        self.dosage_entry = CTkEntry(self)
        self.dosage_entry.grid(row=2, column=1, sticky="w")

        self.frequency_label = CTkLabel(self, text="Frequency")
        self.frequency_label.grid(row=3, column=0, sticky="w")

        self.frequency_entry = CTkEntry(self)
        self.frequency_entry.grid(row=3, column=1, sticky="w")

        self.duration_label = CTkLabel(self, text="Duration")
        self.duration_label.grid(row=4, column=0, sticky="w")

        self.duration_entry = CTkEntry(self)
        self.duration_entry.grid(row=4, column=1, sticky="w")

        self.route_label = CTkLabel(self, text="Route")
        self.route_label.grid(row=5, column=0, sticky="w")

        self.route_entry = CTkEntry(self)
        self.route_entry.grid(row=5, column=1, sticky="w")

        self.reason_label = CTkLabel(self, text="Reason")
        self.reason_label.grid(row=6, column=0, sticky="w")

        self.reason_entry = CTkEntry(self)
        self.reason_entry.grid(row=6, column=1, sticky="w")

        # self.prescribed_by_label = CTkLabel(self, text="Prescribed By")
        # self.prescribed_by_label.pack(side=TOP, padx=5, pady=5)

        # self.prescribed_by_entry = CTkEntry(self)
        # self.prescribed_by_entry.pack(side=TOP, padx=5, pady=5)

        submit_button = CTkButton(self, text="Submit", command=self.submit)
        submit_button.grid(row=7, column=0, sticky="nsew", columnspan=2)

    def get_entry(self):
        entry = MedicationEntry(
            date=self.date_entry.get(),
            medication_name=self.name_entry.get(),
            dosage=self.dosage_entry.get(),
            frequency=self.frequency_entry.get(),
            duration=self.duration_entry.get(),
            route=self.route_entry.get(),
            reason=self.reason_entry.get())

        return entry

    def submit(self):
        entry = self.get_entry()
        if self.controller:
            self.controller.nev_submit_entry(entry)


class EditEntryView(Page):
    entry: Entry = None

    def __init__(self, parent, controller: Controller = None, entry: Entry = None):
        super().__init__(parent)

        if entry is not None:
            self.entry = entry

        self.set_controller(controller)

        self.frame1 = CTkFrame(self)
        self.frame1.pack(fill=X, expand=True, padx=20, pady=40)

        self.entry_type_label = CTkLabel(self.frame1, text="Entry Type")
        self.entry_type_label.pack(side=TOP, padx=5, pady=5)

        entry_types = [entry_type.name for entry_type in EntryType]
        self.entry_type_entry = CTkComboBox(
            self.frame1, values=entry_types, command=self.entry_type_selected)
        self.entry_type_entry.pack(side=TOP, padx=5, pady=5)

        self.frame2 = None

        self.update()

    def entry_type_selected(self, event=None):
        entry_type = self.entry_type_entry.get()
        if entry_type == EntryType.MEDICATION.name:
            if not self.entry or self.entry.entry_type != EntryType.MEDICATION:
                self.entry = MedicationEntry()

        self.update()

    def update(self):
        if self.entry:
            self.entry_type_entry.set(self.entry.entry_type.name)
            if self.entry.entry_type == EntryType.MEDICATION:
                self.frame2 = MedicationEntryForm(
                    self, controller=self.controller, entry=self.entry)
                self.frame2.pack(fill=X, expand=True, padx=20, pady=40)

    def set_controller(self, controller: Controller):
        self.controller = controller

    def submit(self):
        if self.controller and self.frame2:
            entry = self.frame2.get_entry()
            self.controller.nev_submit_entry(entry)
