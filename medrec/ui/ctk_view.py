from medrec.controller import Controller
from customtkinter import CTk, CTkFrame
from medrec.entry import Entry
from medrec.ui.entry_detail_view import EntryDetailView
from medrec.ui.home_view import HomeView
from medrec.ui.edit_entry_view import EditEntryView
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

    def set_main_page(self):
        self.current_page.destroy()
        self.current_page = HomeView(self.root, controller=self.controller)
        self.current_page.show()

    def set_new_entry_page(self):
        self.current_page.destroy()
        self.current_page = EditEntryView(
            self.root, controller=self.controller)
        self.current_page.show()

    def set_view_entries_page(self, entries: list[Entry], display_count, entry_count, start_index):
        self.current_page.destroy()
        self.current_page = EntryListView(
            self.root, controller=self.controller, entries=entries, display_count=display_count, entry_count=entry_count, start_index=start_index)
        self.current_page.show()

    def set_edit_entry_page(self, entry: Entry):
        self.current_page.destroy()
        self.current_page = EditEntryView(
            self.root, controller=self.controller, entry=entry)
        self.current_page.show()

    def set_view_entry_page(self, entry: Entry):
        self.current_page.destroy()
        self.current_page = EntryDetailView(
            self.root, controller=self.controller, entry=entry)
        self.current_page.show()

    def exit(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()
