# from model import Model
from abc import ABC, abstractmethod
from enum import Enum

class PageType(Enum):
    """The pages in the application."""
    MAIN_PAGE = 0
    VIEW_ENTRIES_PAGE = 1
    ADD_ENTRY_PAGE = 2
    EDIT_ENTRY_PAGE = 3

class View(ABC):
    """The view of the application."""
    page_history = []
        
    @abstractmethod
    def update(self, data=None):
        """Update the view."""



