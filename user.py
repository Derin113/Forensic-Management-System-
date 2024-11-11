# Easily Navigate to Change Key -- verify --

from tkinter import *
from tkinter import ttk
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="fms"
)

class Case:
    def __init__(self, connection):
        self.con = connection

    def add(self, UserID, Password, Role):
        res = self.con.cursor()
        sql = "INSERT INTO User (UserID, Password, Role) VALUES (%s, %s, %s)"
        user = (UserID, Password, Role)
        res.execute(sql, user)
        self.con.commit()

    def update(self, UserID, Password, Role):
        res = self.con.cursor()
        sql = "UPDATE User SET Password=%s, Role=%s WHERE UserID=%s"
        user = (Password, Role, UserID)
        res.execute(sql, user)
        self.con.commit()

    def delete(self, UserID):
        res = self.con.cursor()
        sql = "DELETE FROM User WHERE UserID = %s"
        user = (UserID,)
        res.execute(sql, user)
        self.con.commit()

    def fetch(self):
        res = self.con.cursor()
        sql = "SELECT * FROM User"
        res.execute(sql)
        result = res.fetchall()
        return result

class UserManagement:
    def __init__(self, main_frame):
        self.case_inst = Case(con)

        self.user_frame = Frame(main_frame, bg="#535c68")
        self.user_frame.place(x=0, y=30, width=1000, height=480)

        Label(self.user_frame, text="User ID", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=0, column=0, padx=(18,5), pady=10, sticky="w")
        self.txtUserID = Entry(self.user_frame, font=("Calibri", 16), width=20)
        self.txtUserID.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        Label(self.user_frame, text="Password", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=0, column=2, padx=(18,5), pady=10, sticky="w")
        self.txtPassword = Entry(self.user_frame, font=("Calibri", 16), width=20, show="*")
        self.txtPassword.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        Label(self.user_frame, text="Role", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=0, column=4, padx=(18,5), pady=10, sticky="w")
        self.txtRole = Entry(self.user_frame, font=("Calibri", 16), width=20)
        self.txtRole.grid(row=0, column=5, padx=10, pady=10, sticky="w")

        btn_frame = Frame(main_frame, bg="#535c68")
        btn_frame.place(x=250, y=110, width=500, height=40)
        Button(btn_frame, command=self.add_user, text="Add User", width=15, font=("Calibri", 14, "bold"), fg="white", bg="#16a085", bd=0).grid(row=0, column=0, padx=5)
        Button(btn_frame, command=self.update_user, text="Update User", width=15, font=("Calibri", 14, "bold"), fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=5)
        Button(btn_frame, command=self.delete_user, text="Delete User", width=15, font=("Calibri", 14, "bold"), fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=5)

        self.case_table_frame = Frame(main_frame, bg="#ecf0f1")
        self.case_table_frame.place(x=10, y=180, width=980, height=310)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tv = ttk.Treeview(self.case_table_frame, columns=(1, 2, 3), style="mystyle.Treeview")
        for col in range(1, 4):
            self.tv.column(col, anchor='center')
        self.tv.heading("1", text="User ID")
        self.tv.heading("2", text="Password")
        self.tv.heading("3", text="Role")
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.get_data)
        self.tv.pack(fill=X)
        self.display_all()

    def display_all(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.case_inst.fetch():
            self.tv.insert("", END, values=row)

    def add_user(self):
        self.case_inst.add(
            self.txtUserID.get(),
            self.txtPassword.get(),
            self.txtRole.get()
        )
        self.display_all()

    def update_user(self):
        self.case_inst.update(
            self.txtUserID.get(),
            self.txtPassword.get(),
            self.txtRole.get()
        )
        self.display_all()

    def delete_user(self):
        self.case_inst.delete(self.txtUserID.get())
        self.display_all()

    def clear_all(self):
        self.txtUserID.delete(0, END)
        self.txtPassword.delete(0, END)
        self.txtRole.delete(0, END)

    def get_data(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        row = data["values"]
        if row:
            self.txtUserID.delete(0, END)
            self.txtUserID.insert(END, row[0])
            self.txtPassword.delete(0, END)
            self.txtPassword.insert(END, row[1])
            self.txtRole.delete(0, END)
            self.txtRole.insert(END, row[2])

def main_app():
    def center_window(window, width=1000, height=500):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def verify():
        if entry_admin_key.get() == "12345":
            admin_frame.pack_forget()
            UserManagement(main_frame)
        # else:
            # messagebox.showerror("Error", "Invalid Admin Key")

    admin_window = Tk()
    admin_window.title("Admin Login")

    center_window(admin_window)

    main_frame = Frame(admin_window, bg="#535c68")
    main_frame.pack(fill=BOTH, expand=True)

    admin_frame = Frame(main_frame, bg="#535c68")
    admin_frame.place(x=10, y=10, width=980, height=480)

    Label(admin_frame, text="Enter Admin Key:", font=("Calibri", 24), bg="#535c68", fg="white").pack(pady=20)
    entry_admin_key = Entry(admin_frame, font=("Calibri", 24), show="*",bg="white", fg="#535c68",bd=0)
    entry_admin_key.pack(pady=20)

    Button(admin_frame, text="Login", command=verify, font=("Calibri", 16)).pack(pady=20)

    admin_window.mainloop()

# if __name__ == "__main__":
#     con.close()
