from tkinter import *
import mysql.connector
import user

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="fms"
)

class Validate:
    def __init__(self, connection):
        self.con = connection

    def check(self, UserId, password):
        cursor = self.con.cursor()
        sql = "SELECT CASE WHEN EXISTS (SELECT 1 FROM User WHERE UserID = %s) THEN 'True' ELSE 'False' END AS result;"
        cursor.execute(sql, (UserId,))
        result = cursor.fetchone()
        cursor.close()

        if result[0] == 'True':
            cursor = self.con.cursor()
            sql = "SELECT Password FROM User WHERE UserID = %s"
            cursor.execute(sql, (UserId,))
            result_pass = cursor.fetchone()
            cursor.close()

            if result_pass and password == result_pass[0]:
                # messagebox.showinfo("Access", "Access Granted")
                return True
            else:
                # messagebox.showerror("Access Denied", "Wrong Password. Access Denied")
                return False
        else:
            # messagebox.showerror("Access Denied", "Wrong User ID. Access Denied")
            return False

class MainApplication0:
    def __init__(self, start, show_main_callback):
        self.show_main_callback = show_main_callback

        self.root0 = start
        self.root0.title("Forensic Management System")
        self.root0.config(bg="white")
        self.root0.state("zoomed")

        self.header = Frame(self.root0, bg="#2a2e34")
        self.header.place(x=0, y=0, width=1540, height=850)

        self.top_option = Frame(self.header, bg="#2a2e34")
        self.top_option.place(x=10, y=10, width=1510, height=50)

        self.Modify_user = Button(self.top_option, text="Modify User", font=("Calibri", 14, "bold"), fg="white", bg="green", bd=0,pady=3, padx=20, command=self.open_modify_user_window)
        self.Modify_user.place(x=0, y=0)

        self.close = Button(self.top_option, text="Exit", font=("Calibri", 14, "bold"), fg="white", bg="red", bd=0,pady=3, padx=20, command=self.exit_program)
        self.close.place(x=1430, y=0)

        self.header_name = Frame(self.root0, bg="#2a2e34")
        self.header_name.place(x=10, y=150, width=1510, height=140)

        self.title = Label(self.header_name, text="Forensic Management System", font=("Calibri", 80, "bold"),bg="#2a2e34", fg="white", pady=10)
        self.title.place(x=100, y=-10)

        self.entry_frame = Frame(self.root0, bg="#2a2e34")
        self.entry_frame.place(x=500, y=400, width=540, height=250)

        lblUserId = Label(self.entry_frame, text="User ID", font=("Calibri", 20), bg="#2a2e34", fg="white")
        lblUserId.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txtUserID = Entry(self.entry_frame, font=("Calibri", 20), width=20)
        self.txtUserID.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        lblPassword = Label(self.entry_frame, text="Password", font=("Calibri", 20), bg="#2a2e34", fg="white")
        lblPassword.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtPassword = Entry(self.entry_frame, font=("Calibri", 20), show="*")
        self.txtPassword.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.Submit = Button(self.entry_frame, text="Submit", font=("Calibri", 14, "bold"), fg="black", bg="grey", bd=0,
                             pady=3, padx=20, command=self.submit)
        self.Submit.place(x=230, y=170)

        self.validator = Validate(con)

    def submit(self):
        UserID = int(self.txtUserID.get())
        password = self.txtPassword.get()
        if self.validator.check(UserID, password):
            self.show_main_callback()

    def exit_program(self):
        self.root0.destroy()

    def open_modify_user_window(self):
        user.main_app()

# if __name__ == "__main__":
#     root = Tk()
#     app = MainApplication0(root, None)
#     root.mainloop()
#     con.close()
