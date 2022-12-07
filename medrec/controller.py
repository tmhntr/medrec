from uuid import UUID
from medrec.model import Model
from medrec.entry import Entry, EntryType
from medrec.view import View, PageType


class Controller:
    previous_page = None
    current_page = None

    def __init__(self, model: Model, view: View = None):
        self.model: Model = model

        self.view: View = view

    def update_view(self):
        page = self.model.get_page()
        if page == PageType.MAIN_PAGE:
            self.view.set_main_page()
        elif page == PageType.VIEW_ENTRIES_PAGE:
            entries, display_count, entry_count, start_index = self.get_view_entries_page_data()
            self.view.set_view_entries_page(
                entries=entries, display_count=display_count, entry_count=entry_count, start_index=start_index)
        elif page == PageType.EDIT_ENTRY_PAGE:
            entry = self.get_edit_entry_page_data()
            self.view.set_edit_entry_page(entry)
        elif page == PageType.VIEW_ENTRY_PAGE:
            data = self.get_view_entry_page_data()
            self.view.set_view_entry_page(data)

    def get_view_entries_page_data(self):
        index = self.model.entry_view_model.get_entry_index()
        display_count = self.model.entry_view_model.get_display_number()

        entries = self.model.get_entries(limit=display_count, offset=index)
        entry_count = self.model.get_entry_count()
        start_index = index
        return entries, display_count, entry_count, start_index

    def get_edit_entry_page_data(self):
        return self.model.get_current_entry()

    def get_view_entry_page_data(self):
        data = {}
        entry_id = self.model.get_current_entry()
        entry = self.model.get_entry(entry_id)
        data["entry"] = entry
        return data

    def set_page(self, page: PageType):
        self.model.set_page(page)
        self.update_view()

    def get_page(self):
        return self.model.get_page()

    def get_current_entry(self):
        return self.model.get_current_entry()

    def set_current_entry(self, entry_id: str):
        self.model.set_current_entry(entry_id)

    def nev_submit_entry(self, entry: Entry):
        # TODO: Validate data
        self.model.add_entry(entry)
        self.model.set_page(PageType.MAIN_PAGE)
        self.update_view()

    def elv_next_button_clicked(self):
        self.model.entry_view_model.entry_index += self.model.entry_view_model.display_number
        self.update_view()

    def elv_previous_button_clicked(self):
        self.model.entry_view_model.entry_index -= self.model.entry_view_model.display_number
        self.update_view()

    def set_page(self, page_name: str):
        self.model.set_page(page_name)
        self.update_view()

    def back(self):
        self.model.back_page()
        self.update_view()

    def edit_entry(self, entry_id: str):
        self.model.set_page(PageType.EDIT_ENTRY_PAGE)
        entry = self.model.get_entry(entry_id)
        self.view.set_edit_entry_page(entry)
