# a tk frame to input an entry

from tkinter import Frame, Label, StringVar, ttk
from tkinter import Entry as TkEntry
from ..entry import Entry, EntryType, HealthcareWorkerType, HealthcareWorkers

class HealthcareWorkerInput(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.healthcare_worker = HealthcareWorkers(name="Dr. Test", role=HealthcareWorkerType.DOCTOR)
        self.healthcare_worker_role = StringVar(self)
        self.healthcare_worker_role.set(self.healthcare_worker.role.name)
        self.healthcare_worker_role_box = ttk.Combobox(self, width=30, textvariable=self.healthcare_worker_role, state='readonly')
        self.healthcare_worker_role_box['values'] = [healthcare_worker_role.name for healthcare_worker_role in HealthcareWorkerType]
        self.healthcare_worker_role_box.grid(row=0, column=0, padx=5)
        self.healthcare_worker_role_box.bind("<<ComboboxSelected>>", self.onHealthcareWorkerRoleChange)

        self.name_label = Label(self, text="Name")
        self.name_label.grid(row=1, column=0, padx=5)
        self.name_entry = TkEntry(self)
        self.name_entry.grid(row=1, column=1, padx=5)
        self.name_entry.insert(0, self.healthcare_worker.name)

    def onHealthcareWorkerRoleChange(self, event):
        self.healthcare_worker.role = HealthcareWorkerType[self.healthcare_worker_role.get()]
        print(self.healthcare_worker.role)




class EntryInput(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.entry = Entry()
        self.entry_type = StringVar(self)
        self.entry_type.set(self.entry.entry_type.name)
        self.entry_type_box = ttk.Combobox(self, width=30, textvariable=self.entry_type, state='readonly')
        self.entry_type_box['values'] = [entry_type.name for entry_type in EntryType]
        self.entry_type_box.grid(row=0, column=0, padx=5)
        self.entry_type_box.bind("<<ComboboxSelected>>", self.onEntryTypeChange)

        self.date_label = Label(self, text="Date")
        self.date_label.grid(row=1, column=0, padx=5)
        self.date_entry = TkEntry(self)
        self.date_entry.grid(row=1, column=1, padx=5)
        self.date_entry.insert(0, self.entry.date)

        self.time_label = Label(self, text="Time")
        self.time_label.grid(row=2, column=0, padx=5)
        self.time_entry = TkEntry(self)
        self.time_entry.grid(row=2, column=1, padx=5)
        self.time_entry.insert(0, self.entry.time)

        self.location_label = Label(self, text="Location")
        self.location_label.grid(row=3, column=0, padx=5)
        self.location_entry = TkEntry(self)
        self.location_entry.grid(row=3, column=1, padx=5)
        self.location_entry.insert(0, self.entry.location)

        self.description_label = Label(self, text="Description")
        self.description_label.grid(row=4, column=0, padx=5)
        self.description_entry = TkEntry(self)
        self.description_entry.grid(row=4, column=1, padx=5)
        self.description_entry.insert(0, self.entry.description)

        self.healthcare_worker_label = Label(self, text="Healthcare Worker")
        self.healthcare_worker_label.grid(row=5, column=0, padx=5)
        self.healthcare_worker_input = HealthcareWorkerInput(self)
        self.healthcare_worker_input.grid(row=5, column=1, padx=5)

        self.health_data_label = Label(self, text="Health Data")
        self.health_data_label.grid(row=6, column=0, padx=5)
        self.health_data_entry = TkEntry(self)
        self.health_data_entry.grid(row=6, column=1, padx=5)
        self.health_data_entry.insert(0, self.entry.health_data)

    def onEntryTypeChange(self, event):
        self.entry.entry_type = EntryType[self.entry_type.get()]
        print(self.entry.entry_type)


