from medrec.controller import Controller
from customtkinter import CTk, CTkFrame
from medrec.ui.home_view import HomeView
from medrec.ui.new_entry_view import NewEntryView
from medrec.ui.entry_list_view import EntryListView
from medrec.view import PageType, View
from medrec.ui.page import Page
TITLE = "MediTrack"
VERSION = "0.1.0"


class CTkView(View):
    current_page_type: PageType = PageType.MAIN_PAGE
    data = {}

    def __init__(self, controller: Controller = None):
        super().__init__()
        self.root = CTk()
        self.root.title(TITLE + " " + VERSION)
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.controller = controller

        self.current_page: Page = HomeView(
            self.root, controller=self.controller)
        self.current_page.show()

    def set_controller(self, controller: Controller):
        self.controller = controller
        self.current_page.set_controller(controller)

    def update(self, data=None):
        """Update the UI."""
        next_page_type: PageType = data.get("page")
        if next_page_type == self.current_page_type:
            self.current_page.update(data)
        else:
            self.current_page.destroy()

            self.current_page_type = next_page_type

            if next_page_type == PageType.MAIN_PAGE:
                self.current_page = HomeView(
                    self.root, controller=self.controller)
            elif next_page_type == PageType.ADD_ENTRY_PAGE:
                self.current_page = NewEntryView(
                    self.root, controller=self.controller)
            elif next_page_type == PageType.VIEW_ENTRIES_PAGE:
                self.current_page = EntryListView(
                    self.root, controller=self.controller)
            else:
                self.current_page = HomeView(
                    self.root, controller=self.controller)

            self.current_page.update(data)
            self.current_page.show()

    def exit(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()
