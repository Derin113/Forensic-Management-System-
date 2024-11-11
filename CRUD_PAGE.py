from tkinter import ttk
from tkinter import *
from Case import Case, con
from Evidence import Evidence, con
from Suspect import Suspect, con
from Witness import Witness, con
from DeleteAll import Delete,con
from tkcalendar import DateEntry
class Case_g:
    def __init__(self, case_frame):
        self.case_f = case_frame
        self.case_inst = Case(con)

        self.case_inst1 = Case(con)
        self.evidence_inst1 = Evidence(con)
        self.suspect_inst1 = Suspect(con)
        self.witness_inst1 = Witness(con)
        self.delete_all_inst = Delete(con)

        self.case_ef = Frame(case_frame, bg="#535c68")
        self.case_ef.place(x=10, y=10, width=1480, height=160)

        self.title = Label(self.case_ef, text="Case List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

        lblCaseID = Label(self.case_ef, text="Case ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblCaseID.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtCaseID = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtCaseID.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lblCaseName = Label(self.case_ef, text="Case Name", font=("Calibri", 16), bg="#535c68", fg="white")
        lblCaseName.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txtCaseName = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtCaseName.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lblLeadInv = Label(self.case_ef, text="Lead Investigator", font=("Calibri", 16), bg="#535c68", fg="white")
        lblLeadInv.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txtLeadInv = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtLeadInv.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        lblStatus = Label(self.case_ef, text="Status", font=("Calibri", 16), bg="#535c68", fg="white")
        lblStatus.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.comboStatus = ttk.Combobox(self.case_ef, font=("Calibri", 16), width=28, state="readonly")
        self.comboStatus['values'] = ("Open", "Closed", "Archived")
        self.comboStatus.grid(row=2, column=3, padx=10, sticky="w")

        # lblDateOpened = Label(self.case_ef, text="Date Opened", font=("Calibri", 16), bg="#535c68", fg="white")
        # lblDateOpened.grid(row=1, column=4, padx=10, pady=10, sticky="w")
        # self.txtDateOpened = Entry(self.case_ef, font=("Calibri", 16), width=30)
        # self.txtDateOpened.grid(row=1, column=5, padx=10, pady=10, sticky="w")

        lblDateOpened = Label(self.case_ef, text="Date Opened", font=("Calibri", 16), bg="#535c68", fg="white")
        lblDateOpened.grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.txtDateOpened = DateEntry(self.case_ef, font=("Calibri", 16), width=20,selectmode='none',date_pattern='dd/mm/yyyy')
        self.txtDateOpened.delete(0, 'end')
        self.txtDateOpened.grid(row=1, column=5, padx=10, pady=10, sticky="w")
        bt1 = Button(self.case_ef, text="Clear", command=lambda : self.txtDateOpened.delete(0, 'end'),width=8,font=("Calibri", 12),fg="white", bg="black", bd=0)
        bt1.grid(row=1,column=6,padx=10, pady=0, sticky="w")

        lblDateClosed = Label(self.case_ef, text="Date Closed", font=("Calibri", 16), bg="#535c68", fg="white")
        lblDateClosed.grid(row=2, column=4, padx=10, pady=10, sticky="w")
        self.txtDateClosed = DateEntry(self.case_ef, font=("Calibri", 16), width=20,selectmode='none',date_pattern='dd/mm/yyyy',)
        self.txtDateClosed.delete(0, 'end')
        self.txtDateClosed.grid(row=2, column=5, padx=10, pady=10, sticky="w")
        bt1 = Button(self.case_ef, text="Clear", command=lambda: self.txtDateClosed.delete(0, 'end'), width=8,font=("Calibri", 12), fg="white", bg="black", bd=0)
        bt1.grid(row=2, column=6, padx=10, pady=0, sticky="w")


        # lblDateClosed = Label(self.case_ef, text="Date Closed", font=("Calibri", 16), bg="#535c68", fg="white")
        # lblDateClosed.grid(row=2, column=4, padx=10, pady=10, sticky="w")
        # self.txtDateClosed = Entry(self.case_ef, font=("Calibri", 16), width=10)
        # self.txtDateClosed.grid(row=2, column=5, padx=10, pady=10, sticky="w")




        self.btn_frame = Frame(case_frame, bg="#535c68")
        self.btn_frame.place(x=230, y=190, width=1050, height=40)

        btnAdd = Button(self.btn_frame, command=self.add_case, text="Add Case", width=15, font=("Calibri", 14, "bold"),fg="white", bg="#16a085", bd=0)
        btnAdd.grid(row=0, column=0, padx=25)

        btnEdit = Button(self.btn_frame, command=self.update_case, text="Update Case", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#2980b9", bd=0)
        btnEdit.grid(row=0, column=1, padx=25,)

        btnDelete = Button(self.btn_frame, command=self.delete_case, text="Delete Case", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#c0392b", bd=0)
        btnDelete.grid(row=0, column=2, padx=25)

        btnClear = Button(self.btn_frame, command=self.clear_all, text="Clear Details", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#f39c12", bd=0)
        btnClear.grid(row=0, column=3, padx=25)

        btnDeleteAll = Button(self.btn_frame, command=self.deletAll, text="Delete All", width=15,font=("Calibri", 14, "bold"), fg="white", bg="red", bd=0)
        btnDeleteAll.grid(row=0, column=4, padx=25)

        self.case_table_frame = Frame(case_frame, bg="#ecf0f1")
        self.case_table_frame.place(x=10, y=250, width=1490, height=370)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35,)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tv = ttk.Treeview(self.case_table_frame, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
        for col in range(1, 7):
            self.tv.column(col, anchor='center')

        self.tv.heading("1", text="Case ID")
        self.tv.heading("2", text="Case Name")
        self.tv.heading("3", text="Lead Investigator")
        self.tv.heading("4", text="Status")
        self.tv.heading("5", text="Date Opened")
        self.tv.heading("6", text="Date Closed")
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill=X)
        self.displayAll()

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.case_inst.fetch():
            self.tv.insert("", END, values=row)

    def add_case(self):
        self.case_inst.add(
            self.txtCaseID.get(),
            self.txtCaseName.get(),
            self.txtLeadInv.get(),
            self.comboStatus.get(),
            self.txtDateOpened.get(),
            self.txtDateClosed.get()
        )
        self.displayAll()
        self.clear_all()

    def update_case(self):
        self.case_inst.update(
            self.txtCaseID.get(),
            self.txtCaseName.get(),
            self.txtLeadInv.get(),
            self.comboStatus.get(),
            self.txtDateOpened.get(),
            self.txtDateClosed.get()
        )
        self.displayAll()
        self.clear_all()

    def delete_case(self):
        self.case_inst.delete(self.txtCaseID.get())
        self.displayAll()
        self.clear_all()

    def deletAll(self):
        self.delete_all_inst.delete_case(self.txtCaseID.get())
        self.displayAll()
        self.clear_all()

    def clear_all(self):
        self.txtCaseID.delete(0, END)
        self.txtCaseName.delete(0, END)
        self.txtLeadInv.delete(0, END)
        self.comboStatus.set("")
        self.txtDateOpened.delete(0, END)
        self.txtDateClosed.delete(0, END)

    def getData(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        row = data["values"]
        if row:
            self.txtCaseID.delete(0, END)
            self.txtCaseID.insert(END, row[0])
            self.txtCaseName.delete(0, END)
            self.txtCaseName.insert(END, row[1])
            self.txtLeadInv.delete(0, END)
            self.txtLeadInv.insert(END, row[2])
            self.comboStatus.set(row[3])
            self.txtDateOpened.delete(0, END)
            self.txtDateOpened.insert(END, row[4])
            self.txtDateClosed.delete(0, END)
            self.txtDateClosed.insert(END, row[5])

class Evidence_g:
    def __init__(self, evidence_frame):

        self.evidence_f = evidence_frame
        self.evidence_inst = Evidence(con)

        self.evidence_ef = Frame(evidence_frame, bg="#535c68")
        self.evidence_ef.place(x=10, y=10, width=1480, height=160)

        self.title = Label(self.evidence_ef, text="Evidence List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

        lblEvidenceID = Label(self.evidence_ef, text="Evidence ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblEvidenceID.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtEvidenceID = Entry(self.evidence_ef, font=("Calibri", 14), width=13)
        self.txtEvidenceID.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lblCaseID = Label(self.evidence_ef, text="Case ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblCaseID.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txtCaseID = Entry(self.evidence_ef, font=("Calibri", 14), width=13)
        self.txtCaseID.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lblCollectedBy = Label(self.evidence_ef, text="Collected By", font=("Calibri", 16), bg="#535c68", fg="white")
        lblCollectedBy.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txtCollectedBy = Entry(self.evidence_ef, font=("Calibri", 14), width=19)
        self.txtCollectedBy.grid(row=1, columnspan=2,column=3, padx=10, pady=10, sticky="w")

        # lblDateClosed = Label(self.case_ef, text="Date Closed", font=("Calibri", 16), bg="#535c68", fg="white")
        # lblDateClosed.grid(row=2, column=4, padx=10, pady=10, sticky="w")
        # self.txtDateClosed = DateEntry(self.case_ef, font=("Calibri", 16), width=20, selectmode='none',date_pattern='dd/mm/yyyy', )
        # self.txtDateClosed.delete(0, 'end')
        # self.txtDateClosed.grid(row=2, column=5, padx=10, pady=10, sticky="w")
        # bt1 = Button(self.case_ef, text="Clear", command=lambda: self.txtDateClosed.delete(0, 'end'), width=8,font=("Calibri", 12), fg="white", bg="black", bd=0)
        # bt1.grid(row=2, column=6, padx=10, pady=0, sticky="w")

        lblDateCollected = Label(self.evidence_ef, text="Date Collected", font=("Calibri", 16), bg="#535c68", fg="white")
        lblDateCollected.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.txtDateCollected = DateEntry(self.evidence_ef, font=("Calibri", 16), width=12, selectmode='none',date_pattern='dd/mm/yyyy', )
        self.txtDateCollected.delete(0, 'end')
        self.txtDateCollected.grid(row=2, column=3, padx=(10,1), pady=10, sticky="w")
        bt1 = Button(self.evidence_ef, text="Clr", command=lambda: self.txtDateCollected.delete(0, 'end'), width=3,
                     font=("Calibri", 12), fg="white", bg="black", bd=0)
        bt1.grid(row=2, column=4, padx=0, pady=0, sticky="w")

        # lblDateCollected = Label(self.evidence_ef, text="Date Collected", font=("Calibri", 16), bg="#535c68",fg="white")
        # lblDateCollected.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        # self.txtDateCollected = Entry(self.evidence_ef, font=("Calibri", 14), width=17)
        # self.txtDateCollected.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        lblStorageLocation = Label(self.evidence_ef, text="Storage Location", font=("Calibri", 16), bg="#535c68", fg="white")
        lblStorageLocation.grid(row=1, column=5, padx=10, pady=10, sticky="w")
        self.txtStorageLocation = Entry(self.evidence_ef, font=("Calibri", 14), width=20)
        self.txtStorageLocation.grid(row=1, column=6, padx=10, pady=10, sticky="w")

        lblLocation = Label(self.evidence_ef, text="Location", font=("Calibri", 16), bg="#535c68", fg="white")
        lblLocation.grid(row=2, column=5, padx=10, pady=10, sticky="w")
        self.txtLocation = Entry(self.evidence_ef, font=("Calibri", 14), width=20)
        self.txtLocation.grid(row=2, column=6, padx=10, pady=10, sticky="w")

        lblEvidenceType = Label(self.evidence_ef, text="Evidence Type", font=("Calibri", 16), bg="#535c68", fg="white")
        lblEvidenceType.grid(row=1, column=7, padx=10, pady=10, sticky="w")
        self.txtEvidenceType = Entry(self.evidence_ef, font=("Calibri", 14), width=28)
        self.txtEvidenceType.grid(row=1, column=8, padx=10, pady=10, sticky="w")

        lblDescription = Label(self.evidence_ef, text="Description", font=("Calibri", 16), bg="#535c68", fg="white")
        lblDescription.grid(row=2, column=7, padx=10, pady=10, sticky="w")
        self.txtDescription = Entry(self.evidence_ef, font=("Calibri", 14), width=28)
        self.txtDescription.grid(row=2, column=8, padx=10, pady=10, sticky="w")

        self.btn_frame = Frame(evidence_frame, bg="#535c68")
        self.btn_frame.place(x=360, y=190, width=840, height=40)

        btnAdd = Button(self.btn_frame, command=self.add_evidence, text="Add Evidence", width=15, font=("Calibri", 14, "bold"),fg="white", bg="#16a085", bd=0)
        btnAdd.grid(row=0, column=0, padx=25)

        btnEdit = Button(self.btn_frame, command=self.update_evidence, text="Update Evidence", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#2980b9", bd=0)
        btnEdit.grid(row=0, column=1, padx=25)

        btnDelete = Button(self.btn_frame, command=self.delete_evidence, text="Delete Evidence", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#c0392b", bd=0)
        btnDelete.grid(row=0, column=2, padx=25)

        btnClear = Button(self.btn_frame, command=self.clear_all, text="Clear Details", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#f39c12", bd=0)
        btnClear.grid(row=0, column=3, padx=25)

        self.evidence_table_frame = Frame(evidence_frame, bg="#ecf0f1")
        self.evidence_table_frame.place(x=10, y=250, width=1490, height=370)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))

        self.tv = ttk.Treeview(self.evidence_table_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
        for col in range(1, 9):
            self.tv.column(col, anchor='center')

        self.tv.heading("1", text="Ev. ID")
        self.tv.column("1", width=30)
        self.tv.heading("2", text="Case ID")
        self.tv.column("2", width=30)
        self.tv.heading("3", text="D. Collected")
        self.tv.column("3", width=30)
        self.tv.heading("4", text="Collec. By")
        self.tv.column("4", width=30)
        self.tv.heading("5", text="Sto. Location")
        self.tv.column("5", width=100)
        self.tv.heading("6", text="Location")
        self.tv.column("6", width=100)
        self.tv.heading("7", text="Evidence Type")
        self.tv.column("7", width=150)
        self.tv.heading("8", text="Description")
        self.tv.column("8", width=250)
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill=X)
        self.displayAll()

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.evidence_inst.fetch():
            self.tv.insert("", END, values=row)

    def add_evidence(self):
        self.evidence_inst.add(
            self.txtEvidenceID.get(),
            self.txtCaseID.get(),
            self.txtDateCollected.get(),
            self.txtCollectedBy.get(),
            self.txtStorageLocation.get(),
            self.txtLocation.get(),
            self.txtEvidenceType.get(),
            self.txtDescription.get()
        )
        self.displayAll()
        self.clear_all()

    def update_evidence(self):
        self.evidence_inst.update(
            self.txtEvidenceID.get(),
            self.txtCaseID.get(),
            self.txtDateCollected.get(),
            self.txtCollectedBy.get(),
            self.txtStorageLocation.get(),
            self.txtLocation.get(),
            self.txtEvidenceType.get(),
            self.txtDescription.get()
        )
        self.displayAll()
        self.clear_all()

    def delete_evidence(self):
        self.evidence_inst.delete(self.txtEvidenceID.get())
        self.displayAll()
        self.clear_all()

    def clear_all(self):
        self.txtEvidenceID.delete(0, END)
        self.txtCaseID.delete(0, END)
        self.txtDateCollected.delete(0, END)
        self.txtCollectedBy.delete(0, END)
        self.txtStorageLocation.delete(0, END)
        self.txtLocation.delete(0, END)
        self.txtEvidenceType.delete(0, END)
        self.txtDescription.delete(0, END)

    def getData(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        row = data["values"]
        if row:
            self.txtEvidenceID.delete(0, END)
            self.txtEvidenceID.insert(END, row[0])
            self.txtCaseID.delete(0, END)
            self.txtCaseID.insert(END, row[1])
            self.txtDateCollected.delete(0, END)
            self.txtDateCollected.insert(END, row[2])
            self.txtCollectedBy.delete(0, END)
            self.txtCollectedBy.insert(END, row[3])
            self.txtStorageLocation.delete(0, END)
            self.txtStorageLocation.insert(END, row[4])
            self.txtLocation.delete(0, END)
            self.txtLocation.insert(END, row[5])
            self.txtEvidenceType.delete(0, END)
            self.txtEvidenceType.insert(END, row[6])
            self.txtDescription.delete(0, END)
            self.txtDescription.insert(END, row[7])

class Suspect_g:
    def __init__(self, suspect_frame):
        self.suspect_f = suspect_frame
        self.suspect_inst = Suspect(con)

        self.case_ef = Frame(suspect_frame, bg="#535c68")
        self.case_ef.place(x=10, y=10, width=1480, height=160)

        self.title = Label(self.case_ef, text="Suspect List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

        lblSuspectID = Label(self.case_ef, text="Suspect ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblSuspectID.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtSuspectID = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtSuspectID.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lblCaseID = Label(self.case_ef, text="Case ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblCaseID.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txtCaseID = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtCaseID.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lblSuspectName = Label(self.case_ef, text="Suspect Name", font=("Calibri", 16), bg="#535c68", fg="white")
        lblSuspectName.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txtSuspectName = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtSuspectName.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        lblAge = Label(self.case_ef, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
        lblAge.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.txtAge = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtAge.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        lblGender = Label(self.case_ef, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
        lblGender.grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.comboGender = ttk.Combobox(self.case_ef, font=("Calibri", 16), width=28, state="readonly")
        self.comboGender['values'] = ("Male", "Female", "Other")
        self.comboGender.grid(row=1, column=5, padx=10, sticky="w")

        lblAddress = Label(self.case_ef, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
        lblAddress.grid(row=2, column=4, padx=10, pady=10, sticky="w")
        self.txtAddress = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtAddress.grid(row=2, column=5, padx=10, pady=10, sticky="w")

        self.btn_frame = Frame(suspect_frame, bg="#535c68")
        self.btn_frame.place(x=360, y=190, width=840, height=40)

        btnAdd = Button(self.btn_frame, command=self.add_suspect, text="Add Suspect", width=15, font=("Calibri", 14, "bold"),fg="white", bg="#16a085", bd=0)
        btnAdd.grid(row=0, column=0, padx=25)

        btnEdit = Button(self.btn_frame, command=self.update_suspect, text="Update Suspect", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#2980b9", bd=0)
        btnEdit.grid(row=0, column=1, padx=25,)

        btnDelete = Button(self.btn_frame, command=self.delete_suspect, text="Delete Suspect", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#c0392b", bd=0)
        btnDelete.grid(row=0, column=2, padx=25)

        btnClear = Button(self.btn_frame, command=self.clear_all, text="Clear Details", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#f39c12", bd=0)
        btnClear.grid(row=0, column=3, padx=25)

        self.suspect_table_frame = Frame(suspect_frame, bg="#ecf0f1")
        self.suspect_table_frame.place(x=10, y=250, width=1490, height=370)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35,)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tv = ttk.Treeview(self.suspect_table_frame, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
        for col in range(1, 7):
            self.tv.column(col, anchor='center')

        self.tv.heading("1", text="Suspect ID")
        self.tv.column("1", width=100)
        self.tv.heading("2", text="Case ID")
        self.tv.column("2", width=100)
        self.tv.heading("3", text="Suspect Name")
        self.tv.column("3", width=100)
        self.tv.heading("4", text="Age")
        self.tv.column("4", width=100)
        self.tv.heading("5", text="Gender")
        self.tv.column("5", width=100)
        self.tv.heading("6", text="Address")
        self.tv.column("6", width=500)
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill=X)
        self.displayAll()

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.suspect_inst.fetch():
            self.tv.insert("", END, values=row)

    def add_suspect(self):
        self.suspect_inst.add(
            self.txtSuspectID.get(),
            self.txtCaseID.get(),
            self.txtSuspectName.get(),
            self.txtAge.get(),
            self.comboGender.get(),
            self.txtAddress.get()
        )
        self.displayAll()
        self.clear_all()

    def update_suspect(self):
        self.suspect_inst.update(
            self.txtSuspectID.get(),
            self.txtCaseID.get(),
            self.txtSuspectName.get(),
            self.txtAge.get(),
            self.comboGender.get(),
            self.txtAddress.get()
        )
        self.displayAll()
        self.clear_all()

    def delete_suspect(self):
        self.suspect_inst.delete(self.txtSuspectID.get())
        self.displayAll()
        self.clear_all()

    def clear_all(self):
        self.txtSuspectID.delete(0, END)
        self.txtCaseID.delete(0, END)
        self.txtSuspectName.delete(0, END)
        self.txtAge.delete(0, END)
        self.comboGender.set("")
        self.txtAddress.delete(0, END)

    def getData(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        row = data["values"]
        if row:
            self.txtSuspectID.delete(0, END)
            self.txtSuspectID.insert(END, row[0])
            self.txtCaseID.delete(0, END)
            self.txtCaseID.insert(END, row[1])
            self.txtSuspectName.delete(0, END)
            self.txtSuspectName.insert(END, row[2])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, row[3])
            self.comboGender.set(row[4])  # Use set instead of delete and insert for Combobox
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, row[5])

class Witness_g:
    def __init__(self, witness_frame):
        self.witness_f = witness_frame
        self.witness_inst = Witness(con)

        self.case_ef = Frame(witness_frame, bg="#535c68")
        self.case_ef.place(x=10, y=10, width=1480, height=160)

        self.title = Label(self.case_ef, text="Witness List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

        lblWitnessID = Label(self.case_ef, text="Witness ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblWitnessID.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtWitnessID = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtWitnessID.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        lblCaseID = Label(self.case_ef, text="Case ID", font=("Calibri", 16), bg="#535c68", fg="white")
        lblCaseID.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txtCaseID = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtCaseID.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        lblWitnessName = Label(self.case_ef, text="Witness Name", font=("Calibri", 16), bg="#535c68", fg="white")
        lblWitnessName.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txtWitnessName = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtWitnessName.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        lblStatement = Label(self.case_ef, text="Statement", font=("Calibri", 16), bg="#535c68", fg="white")
        lblStatement.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.txtStatement = Entry(self.case_ef, font=("Calibri", 16), width=75)
        self.txtStatement.grid(row=2, column=3, columnspan=3, padx=10, pady=10, sticky="w")

        lblContactInfo = Label(self.case_ef, text="Contact Info", font=("Calibri", 16), bg="#535c68", fg="white")
        lblContactInfo.grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.txtContactInfo = Entry(self.case_ef, font=("Calibri", 16), width=30)
        self.txtContactInfo.grid(row=1, column=5, padx=10, pady=10, sticky="w")

        self.btn_frame = Frame(witness_frame, bg="#535c68")
        self.btn_frame.place(x=360, y=190, width=840, height=40)

        btnAdd = Button(self.btn_frame, command=self.add_witness, text="Add Witness", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#16a085", bd=0)
        btnAdd.grid(row=0, column=0, padx=25)

        btnEdit = Button(self.btn_frame, command=self.update_witness, text="Update Witness", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#2980b9", bd=0)
        btnEdit.grid(row=0, column=1, padx=25)

        btnDelete = Button(self.btn_frame, command=self.delete_witness, text="Delete Witness", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#c0392b", bd=0)
        btnDelete.grid(row=0, column=2, padx=25)

        btnClear = Button(self.btn_frame, command=self.clear_all, text="Clear Details", width=15,font=("Calibri", 14, "bold"), fg="white", bg="#f39c12", bd=0)
        btnClear.grid(row=0, column=3, padx=25)

        self.witness_table_frame = Frame(witness_frame, bg="#ecf0f1")
        self.witness_table_frame.place(x=10, y=250, width=1490, height=370)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tv = ttk.Treeview(self.witness_table_frame, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
        for col in range(1, 6):
            self.tv.column(col, anchor='center')

        self.tv.heading("1", text="Witness ID")
        self.tv.column("1", width=100)
        self.tv.heading("2", text="Case ID")
        self.tv.column("2", width=100)
        self.tv.heading("3", text="Witness Name")
        self.tv.column("3", width=100)
        self.tv.heading("4", text="Contact Info")
        self.tv.column("4", width=100)
        self.tv.heading("5", text="Statement")
        self.tv.column("5", width=500)
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.get_data)
        self.tv.pack(fill=X)
        self.display_all()

    def display_all(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.witness_inst.fetch():
            self.tv.insert("", END, values=row)

    def add_witness(self):
        self.witness_inst.add(
            self.txtWitnessID.get(),
            self.txtCaseID.get(),
            self.txtWitnessName.get(),
            self.txtContactInfo.get(),
            self.txtStatement.get()
        )
        self.display_all()
        self.clear_all()

    def update_witness(self):
        self.witness_inst.update(
            self.txtWitnessID.get(),
            self.txtCaseID.get(),
            self.txtWitnessName.get(),
            self.txtContactInfo.get(),
            self.txtStatement.get()
        )
        self.display_all()
        self.clear_all()

    def delete_witness(self):
        self.witness_inst.delete(self.txtWitnessID.get())
        self.display_all()
        self.clear_all()

    def clear_all(self):
        self.txtWitnessID.delete(0, END)
        self.txtCaseID.delete(0, END)
        self.txtWitnessName.delete(0, END)
        self.txtContactInfo.delete(0, END)
        self.txtStatement.delete(0, END)

    def get_data(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        row = data["values"]
        if row:
            self.txtWitnessID.delete(0, END)
            self.txtWitnessID.insert(END, row[0])
            self.txtCaseID.delete(0, END)
            self.txtCaseID.insert(END, row[1])
            self.txtWitnessName.delete(0, END)
            self.txtWitnessName.insert(END, row[2])
            self.txtContactInfo.delete(0, END)
            self.txtContactInfo.insert(END, row[3])
            self.txtStatement.delete(0, END)
            self.txtStatement.insert(END, row[4])



class MainApplication:
    def __init__(self, start, show_login_callback, view_case_callback):

        self.show_login_callback = show_login_callback
        self.view_case_callback = view_case_callback

        self.root = start

        self.root.title("Forensic Management System")
        self.root.config(bg="white")
        self.root.state("zoomed")

        self.header = Frame(self.root, bg="#2a2e34")
        self.header.place(x=0, y=0, width=1540, height=850)

        self.header_name = Frame(self.root, bg="#2a2e34")
        self.header_name.place(x=10, y=10, width=1520, height=50)

        self.title = Label(self.header_name, text="Forensic Management System", font=("Calibri", 26, "bold"), bg="#2a2e34", fg="white", pady=10)
        self.title.place(x=10, y=-10)

        self.Close_Btn = Button(self.header_name, text="Logout", font=("Calibri", 14, "bold"), fg="white", bg="red", bd=0, pady=3, padx=20, command=self.logout)
        self.Close_Btn.place(x=1400, y=3)

        self.table_name = Frame(self.root, bg="#2a2e34")
        self.table_name.place(x=10, y=80, width=1510, height=50)

        self.case_button = Button(self.table_name, text="Case", font=("Calibri", 14, "bold"), fg="black", bg="white", bd=0, pady=5, padx=30, command=self.show_case_frame)
        self.case_button.grid(row=0, column=0, padx=10)

        self.evidence_button = Button(self.table_name, text="Evidence", font=("Calibri", 14, "bold"), fg="black", bg="white", bd=0, pady=5, padx=30, command=self.show_evidence_frame)
        self.evidence_button.grid(row=0, column=1, padx=10)

        self.suspect_button = Button(self.table_name, text="Suspect", font=("Calibri", 14, "bold"), fg="black", bg="white", bd=0, pady=5, padx=30, command=self.show_suspect_frame)
        self.suspect_button.grid(row=0, column=2, padx=10)

        self.witness_button = Button(self.table_name, text="Witness", font=("Calibri", 14, "bold"), fg="black", bg="white", bd=0, pady=5, padx=30, command=self.show_witness_frame)
        self.witness_button.grid(row=0, column=3, padx=10)

        self.view_case_button = Button(self.table_name, text="View Case", font=("Calibri", 14, "bold"), fg="white", bg="green", bd=0, pady=5, padx=30, command=self.view_case)
        self.view_case_button.grid(row=0, column=4, padx=(770,0))

        self.case_f = Frame(self.root, bg="#535c68")
        self.case_f.place(x=10, y=150, width=1510, height=630)

        self.evidence_f = Frame(self.root, bg="#535c68")
        self.evidence_f.place(x=10, y=150, width=1510, height=630)

        self.suspect_f = Frame(self.root, bg="#535c68")
        self.suspect_f.place(x=10, y=150, width=1510, height=630)

        self.witness_f = Frame(self.root, bg="#535c68")
        self.witness_f.place(x=10, y=150, width=1510, height=630)

        self.case_g_instance = Case_g(self.case_f)
        self.evidence_g_instance = Evidence_g(self.evidence_f)
        self.suspect_g_instance = Suspect_g(self.suspect_f)
        self.witness_g_instance = Witness_g(self.witness_f)
        self.show_case_frame()

    def logout(self):
        self.show_login_callback()

    def view_case(self):
        self.view_case_callback()

    def show_case_frame(self):
        self.case_f.lift()
        self.case_button.config(bg="lightblue")
        self.evidence_button.config(bg="white")
        self.suspect_button.config(bg="white")
        self.witness_button.config(bg="white")

    def show_evidence_frame(self):
        self.evidence_g_instance.displayAll()
        self.evidence_g_instance.clear_all()
        self.evidence_f.lift()
        self.case_button.config(bg="white")
        self.evidence_button.config(bg="lightblue")
        self.suspect_button.config(bg="white")
        self.witness_button.config(bg="white")

    def show_suspect_frame(self):
        self.suspect_g_instance.displayAll()
        self.suspect_g_instance.clear_all()

        self.suspect_f.lift()
        self.case_button.config(bg="white")
        self.evidence_button.config(bg="white")
        self.suspect_button.config(bg="lightblue")
        self.witness_button.config(bg="white")

    def show_witness_frame(self):
        self.witness_g_instance.display_all()
        self.witness_g_instance.clear_all()

        self.witness_f.lift()
        self.case_button.config(bg="white")
        self.evidence_button.config(bg="white")
        self.suspect_button.config(bg="white")
        self.witness_button.config(bg="lightblue")



# if __name__ == "__main__":
#     root = Tk()
#     app = MainApplication(root, None, None)
#     root.mainloop()


