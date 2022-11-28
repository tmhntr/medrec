"""This module contains the GUI for the application."""

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import Scale
from tkinter import Checkbutton
from tkinter import Radiobutton
from tkinter import Entry as TkEntry

from entry import Entry, EntryType, MedicationEntry, HealthcareWorkerType, HealthcareWorkers, HealthData

# a menu bar
class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        fileMenu = Menu(self, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_command(label="Open")
        fileMenu.add_command(label="Save")
        fileMenu.add_command(label="Save as...")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")
        self.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(self, tearoff=0)
        editMenu.add_command(label="Undo")
        editMenu.add_separator()
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_command(label="Delete")
        editMenu.add_separator()
        editMenu.add_command(label="Select All")
        self.add_cascade(label="Edit", menu=editMenu)

        helpMenu = Menu(self, tearoff=0)
        helpMenu.add_command(label="About", command=self.onAbout)
        self.add_cascade(label="Help", menu=helpMenu)

    def onAbout(self):
        messagebox.showinfo("PyPad", "A simple text editor")

        
# a toolbar
class ToolBar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        fontTuple = font.families()
        fontFam = StringVar(self)
        fontFam.set(fontTuple[0])
        fontBox = ttk.Combobox(self, width=30, textvariable=fontFam, state='readonly')
        fontBox['values'] = fontTuple
        fontBox.grid(row=0, column=0, padx=5)
        # fontBox.bind("<<ComboboxSelected>>", self.parent.onFontFamily)

        sizeVar = StringVar(self)
        sizeVar.set("12")
        self.fontSize = Spinbox(self, from_=8, to=72, width=5, textvariable=sizeVar)
        self.fontSize.grid(row=0, column=1, padx=5)
 
        
# a module to input an entry
class EntryInput(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.entry = Entry(date="01/01/2021", description="This is a test entry", entry_type=EntryType.NORMAL, attachments=["test.txt", "test2.txt"], healthcare_workers=[HealthcareWorkers(name="Dr. Test", role=HealthcareWorkerType.DOCTOR)], medications=[MedicationEntry(name="Test", dosage="1", frequency="1", duration="1", route="1", reason="1")], health_data=HealthData(weight=1, height=1, blood_pressure="1", heart_rate=1, respiratory_rate=1, temperature=1))
        self.entry_type = StringVar(master=self)
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

        self.description_label = Label(self, text="Description")
        self.description_label.grid(row=2, column=0, padx=5)
        self.description_entry = scrolledtext.ScrolledText(self, width=40, height=10)
        self.description_entry.grid(row=2, column=1, padx=5)
        self.description_entry.insert(INSERT, self.entry.description)

        self.attachments_label = Label(self, text="Attachments")
        self.attachments_label.grid(row=3, column=0, padx=5)
        self.attachments_entry = TkEntry(self)
        self.attachments_entry.grid(row=3, column=1, padx=5)
        self.attachments_entry.insert(0, ", ".join(self.entry.attachments))

        self.healthcare_workers_label = Label(self, text="Healthcare Workers")
        self.healthcare_workers_label.grid(row=4, column=0, padx=5)
        self.healthcare_workers_entry = TkEntry(self)
        self.healthcare_workers_entry.grid(row=4, column=1, padx=5)
        self.healthcare_workers_entry.insert(0, ", ".join([healthcare_worker.name for healthcare_worker in self.entry.healthcare_workers]))

        self.medications_label = Label(self, text="Medications")
        self.medications_label.grid(row=5, column=0, padx=5)
        self.medications_entry = TkEntry(self)
        self.medications_entry.grid(row=5, column=1, padx=5)
        self.medications_entry.insert(0, ", ".join([medication.name for medication in self.entry.medications]))

        self.health_data_label = Label(self, text="Health Data")
        self.health_data_label.grid(row=6, column=0, padx=5)
        self.health_data_entry = TkEntry(self)
        self.health_data_entry.grid(row=6, column=1, padx=5)
        self.health_data_entry.insert(0, self.entry.health_data)

    def onEntryTypeChange(self, event):
        self.entry.entry_type = EntryType[self.entry_type.get()]
        print(self.entry.entry_type)

# a module to input a healthcare worker
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



# The first frame is the main frame
class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Health Tracker")
        self.pack(fill=BOTH, expand=1)

        # The menu bar
        menuBar = MenuBar(self.parent)
        self.parent.config(menu=menuBar)

        # The toolbar
        toolBar = ToolBar(self.parent)
        toolBar.pack(side=LEFT, fill=Y)

        # the entry frame
        self.entryFrame = EntryInput(self.parent)
        self.entryFrame.pack(side=TOP, fill=BOTH, expand=1)

        # The status bar
        self.statusBar = Label(self, text="Ln 1, Col 1", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

        # The scroll bar
        # scroll = Scrollbar(self.entryFrame)
        # self.entryFrame.config(yscrollcommand=scroll.set)
        # scroll.config(command=self.entryFrame.yview)
        # scroll.pack(side=RIGHT, fill=Y)

        



if __name__ == '__main__':
    root = Tk()
    root.geometry("600x400+300+300")
    app = MainFrame(root)
    root.mainloop()