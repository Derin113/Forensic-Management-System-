from tkinter import *
from LOGIN import MainApplication0
from CRUD_PAGE import MainApplication
from PARTICULAR_CASE_DETAILS import MainApplication1

class AppController:
    def __init__(self):
        self.root = Tk()
        self.show_login()

    def show_login(self):
        self.clear_screen()
        self.login_app = MainApplication0(self.root, self.show_main)

    def show_main(self):
        self.clear_screen()
        self.main_app = MainApplication(self.root, self.show_login, self.show_case_details)

    def show_case_details(self):
        self.clear_screen()
        self.case_details_app = MainApplication1(self.root, self.show_main)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AppController()
    app.run()

