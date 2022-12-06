from abc import ABC, abstractmethod
from tkinter import Frame as CTkFrame

from medrec.controller import Controller


class Page(CTkFrame, ABC):
    """The pages in the application."""
    is_visible = False

    def __init__(self, parent, controller: Controller = None):
        super().__init__(parent)
        self.controller = controller

    @abstractmethod
    def update(self, data=None):
        """Update the UI."""

    def set_controller(self, controller: Controller):
        self.controller = controller

    def show(self):
        self.is_visible = True
        self.pack(fill="both", expand=True)

    def hide(self):
        self.is_visible = False
        self.pack_forget()
