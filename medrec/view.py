# from model import Model
from abc import ABC, abstractmethod
from enum import Enum

from medrec.entry import Entry


class PageType(Enum):
    """The pages in the application."""
    MAIN_PAGE = 0
    VIEW_ENTRIES_PAGE = 1
    EDIT_ENTRY_PAGE = 2
    VIEW_ENTRY_PAGE = 3


class View(ABC):
    """The view of the application."""
    page_history = []

    @abstractmethod
    def set_main_page(self):
        """Set the main page."""
        pass

    @abstractmethod
    def set_view_entries_page(self, entries: list[Entry]):
        """Set the view entries page."""
        pass

    @abstractmethod
    def set_edit_entry_page(self, entry: Entry):
        """Set the edit entry page."""
        pass

    @abstractmethod
    def set_view_entry_page(self, entry: Entry):
        """Set the view entry page."""
        pass
