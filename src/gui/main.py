"""This module contains the GUI for the application."""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import Menu
from tkinter import Spinbox
from tkinter import Scale
from tkinter import Checkbutton
from tkinter import Radiobutton

from src.gui.entry_dialogue import EntryInput

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