from model import Model, data_path
from entry import Entry
from view import View, PageType



class Controller:
    previous_page = None
    current_page = None

    def __init__(self, model: Model, view: View = None):
        self.model: Model = model

        self.view: View = view

    def update_view(self):
        data = self.get_data()
        self.view.update(data)

    def set_page(self, page: PageType):
        self.model.set_page(page)

    def get_page(self):
        return self.model.get_page()

    def get_data(self) -> dict:
        page = self.get_page()
        data = {"page": page}
        if page == PageType.VIEW_ENTRIES_PAGE:
            data.update(self._get_view_entries_data())
        return data

    def _get_view_entries_data(self) -> dict:
        data = {}
        index = self.model.entry_view_model.get_entry_index()
        display_len = self.model.entry_view_model.get_display_number()

        data["entries"] = self._get_entries(index, index + display_len)
        data["entry_count"] = self.model.get_entry_count()
        data["start_index"] = index
        data["display_count"] = display_len
        return data

    def nev_submit_entry(self, data):
        # TODO: Validate data
        entry = Entry(**data)
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

    def _get_entries(self, start_index=0, end_index=None):
        if not end_index:
            return [self.model.get_entry(i) for i in range(start_index, self.model.get_entry_count())]
        return [self.model.get_entry(i) for i in range(start_index, end_index)]

    def back(self):
        self.model.back_page()
        self.update_view()