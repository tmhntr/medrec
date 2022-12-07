from abc import ABC, abstractmethod
from customtkinter import CTkFrame

from medrec.controller import Controller
from medrec.ui.header import Header


class Page(CTkFrame, ABC):
    """The pages in the application."""
    is_visible = False

    def __init__(self, parent, controller: Controller = None, header_text: str = None, has_back_button: bool = True):
        super().__init__(parent)
        self.controller = controller
        self.header = Header(
            self, has_back_button=has_back_button, label=header_text)
        self.header.pack(side="top", fill="x")

    @abstractmethod
    def update(self, data=None):
        """Update the UI."""

    def set_controller(self, controller: Controller):
        self.controller = controller
        self.header.set_controller(controller)

    def show(self):
        self.is_visible = True
        self.pack(fill="both", expand=True)

    def hide(self):
        self.is_visible = False
        self.pack_forget()
