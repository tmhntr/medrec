import customtkinter
from customtkinter import BOTH, LEFT, RIGHT, X, Y

from medrecs.model import Model
from medrecs.controller import Controller


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

data_path = "data.pickle"
   


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Personal Health Record')
        self.geometry('800x600+300+300')

        # create a model
        model = Model("../data/entries.pickle")

        # create a view and place it on the root window
        view = customtkinter.CTkFrame(self)
        view.pack(fill=BOTH, expand=True)

        # create a controller
        controller = Controller(model, view)

        controller.main_page()

        # set the controller to view
        # view.set_controller(controller)

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
