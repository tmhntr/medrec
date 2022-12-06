from medrec.model import Model, data_path
from medrec.controller import Controller
from medrec.ui.ctk_view import CTkView


class App():
    def __init__(self):
        super().__init__()

        self.model = Model(path=data_path)

        self.view = CTkView()

        self.controller = Controller(self.model, view=self.view)

        self.view.set_controller(self.controller)

        self.controller.update_view()

    def mainloop(self):
        self.view.mainloop()


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
