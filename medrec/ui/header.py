from medrec.controller import Controller
from customtkinter import CTkFrame, CTkLabel, CTkButton


class Header(CTkFrame):
    def __init__(self, parent, has_back_button=True, label="default header", controller: Controller = None):
        super().__init__(parent)

        self.set_controller(controller)

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=5)
        # self.grid_columnconfigure(2, weight=1)

        self.label = CTkLabel(self, text=label, font=("Helvetica", 16))
        self.label.pack(side="top", fill="x", padx=24,
                        pady=20, ipady=1, ipadx=1)

        if has_back_button:
            self.button = CTkButton(
                self, text="<-", command=self.back_button_clicked)
            self.button.pack(side="left", padx=24, pady=20, before=self.label)

    def set_controller(self, controller: Controller):
        self.controller = controller

    def back_button_clicked(self):
        if self.controller is not None:
            self.controller.back()
