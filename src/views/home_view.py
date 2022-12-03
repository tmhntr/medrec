import customtkinter
from customtkinter import LEFT, RIGHT, X, Y, BOTH

class HomeView(customtkinter.CTkFrame):
    def __init__(self, parent, controller = None):
        super().__init__(parent)

        # Configure the grid
        self.grid_columnconfigure(0, pad=10)
        self.grid_columnconfigure(1, pad=10)

        self.grid_rowconfigure(0, pad=10)
        self.grid_rowconfigure(1, pad=10)


        # a header for the main frame
        header = customtkinter.CTkLabel(self, text="Personal Health Record", font=("Arial", 20))
        header.pack(fill=X, padx=10, pady=40)

        # a frame for the new entry dialog
        new_entry_frame = customtkinter.CTkFrame(self)
        new_entry_frame.pack(side = LEFT, fill=BOTH, expand=1, padx=20, pady=40)
        heading = customtkinter.CTkLabel(new_entry_frame, text="New Entry", font=("Roboto", 15))
        heading.pack(fill=Y)

        paragraph = customtkinter.CTkLabel(new_entry_frame, text="Create a new entry")
        paragraph.pack(fill=Y)

        self.new_entry_button = customtkinter.CTkButton(new_entry_frame, text="New Entry", command=self.new_entry)
        self.new_entry_button.pack(fill=Y)   

        # a frame for the view entries dialog
        view_entries_frame = customtkinter.CTkFrame(self)
        view_entries_frame.pack(side=RIGHT, fill=BOTH, expand=1, padx=20, pady=40)

        heading = customtkinter.CTkLabel(view_entries_frame, text="View Entries", font=("Roboto", 15))
        heading.pack(fill=Y)

        paragraph = customtkinter.CTkLabel(view_entries_frame, text="View your entries")
        paragraph.pack(fill=Y)

        self.view_entries_button = customtkinter.CTkButton(view_entries_frame, text="View Entries", command=self.view_entries)
        self.view_entries_button.pack(fill=Y)

        self.set_controller(controller)

    def view_entries(self):
        if self.controller:
            self.controller.view_entries_page()

    def new_entry(self):
        if self.controller:
            self.controller.new_entry_page()

    def set_controller(self, controller):
        self.controller = controller
