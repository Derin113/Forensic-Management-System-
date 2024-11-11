import mysql.connector
from CRUD_PAGE import *

con = mysql.connector.connect(host="localhost", user="root", password="12345", database="fms")

class Case_fetch_one:
    def __init__(self, connection):
        self.con = connection

    def fetch(self, CaseID):
        res = self.con.cursor()
        sql = "SELECT * FROM cas_e WHERE CaseID = %s"
        res.execute(sql, (CaseID,))
        result = res.fetchone()
        res.close()
        return result

class Evidence_fetch_one:
    def __init__(self, connection):
        self.con = connection

    def fetch_all_by_case(self, CaseID):
        res = self.con.cursor()
        sql = "SELECT * FROM evidence WHERE CaseID = %s"
        res.execute(sql, (CaseID,))
        result = res.fetchall()
        res.close()
        return result

class Suspect_fetch_one:
    def __init__(self, connection):
        self.con = connection

    def fetch(self, CaseID):
        res = self.con.cursor()
        sql = "SELECT * FROM suspect WHERE CaseID = %s"
        res.execute(sql, (CaseID,))
        result = res.fetchall()
        res.close()
        return result


class Witness_fetch_one:
    def __init__(self, connection):
        self.con = connection

    def fetch(self, CaseID):
        res = self.con.cursor()
        sql = "SELECT * FROM witness WHERE CaseID = %s"
        res.execute(sql, (CaseID,))
        result = res.fetchall()
        res.close()
        return result


class CaseDetailsView:
    def __init__(self, parent, connection):
        self.case_fetch_instance = Case_fetch_one(connection)

        self.case_name_frame = Frame(parent, bg="#535c68")
        self.case_name_frame.place(x=20, y=70, width=1490, height=50)

        self.title = Label(self.case_name_frame, text="Case List", font=("Calibri", 26, "bold"), bg="#535c68",fg="white")
        self.title.place(x=10, y=0)

        self.table_frame = Frame(parent, bg="#535c68")
        self.table_frame.place(x=20, y=120, width=1490, height=70)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tree = ttk.Treeview(self.table_frame, columns=("CaseID", "CaseName", "LeadInvestigator", "Status","DateOpened", "DateClosed"), style="mystyle.Treeview",show='headings')

        self.tree.heading("CaseID", text="CaseID")
        self.tree.heading("CaseName", text="CaseName")
        self.tree.heading("LeadInvestigator", text="LeadInvestigator")
        self.tree.heading("Status", text="Status")
        self.tree.heading("DateOpened", text="DateOpened")
        self.tree.heading("DateClosed", text="DateClosed")
        self.tree.column("CaseID", width=100, anchor='center')
        self.tree.column("CaseName", width=200, anchor='center')
        self.tree.column("LeadInvestigator", width=150, anchor='center')
        self.tree.column("Status", width=100, anchor='center')
        self.tree.column("DateOpened", width=150, anchor='center')
        self.tree.column("DateClosed", width=150, anchor='center')
        self.tree.pack(fill=BOTH, expand=1)

    def fetch_and_display_case_details(self, case_id):
        if case_id:
            case_details = self.case_fetch_instance.fetch(case_id)
            if case_details:
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", "end", values=case_details)
            else:
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", "end", values=("No Case ID Found.",))


class EvidenceDetailsView:
    def __init__(self, parent, connection):
        self.evidence_fetch_instance = Evidence_fetch_one(connection)

        self.evidence_name_frame = Frame(parent, bg="#535c68")
        self.evidence_name_frame.place(x=20, y=190, width=1490, height=50)

        self.title = Label(self.evidence_name_frame, text="Evidence List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.place(x=10, y=0)

        self.table_frame = Frame(parent, bg="#535c68")
        self.table_frame.place(x=20, y=240, width=1490, height=140)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tree = ttk.Treeview(self.table_frame, columns=("EvidenceID", "CaseID", "DateCollected", "CollectedBy", "StorageLocation", "Location", "EvidenceType", "Description"), style="mystyle.Treeview",show='headings')

        self.tree.heading("EvidenceID", text="EvidenceID")
        self.tree.heading("CaseID", text="CaseID")
        self.tree.heading("DateCollected", text="DateCollected")
        self.tree.heading("CollectedBy", text="CollectedBy")
        self.tree.heading("StorageLocation", text="StorageLocation")
        self.tree.heading("Location", text="Location")
        self.tree.heading("EvidenceType", text="EvidenceType")
        self.tree.heading("Description", text="Description")
        self.tree.column("EvidenceID", width=100, anchor='center')
        self.tree.column("CaseID", width=100, anchor='center')
        self.tree.column("DateCollected", width=150, anchor='center')
        self.tree.column("CollectedBy", width=150, anchor='center')
        self.tree.column("StorageLocation", width=200, anchor='center')
        self.tree.column("Location", width=200, anchor='center')
        self.tree.column("EvidenceType", width=150, anchor='center')
        self.tree.column("Description", width=300, anchor='center')
        self.tree.pack(fill=BOTH, expand=1)

    def fetch_and_display_evidence_details(self, case_id):
        if case_id:
            evidence_details = self.evidence_fetch_instance.fetch_all_by_case(case_id)
            if evidence_details:
                self.tree.delete(*self.tree.get_children())
                for evidence in evidence_details:
                    self.tree.insert("", "end", values=evidence)
            else:
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", "end", values=("No evidence.",))


class SuspectDetailsView:
    def __init__(self, parent, connection):
        self.suspect_fetch_instance = Suspect_fetch_one(connection)

        self.Suspect_name_frame = Frame(parent, bg="#535c68")
        self.Suspect_name_frame.place(x=20, y=380, width=1490, height=50)

        self.title = Label(self.Suspect_name_frame, text="Suspect List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.place(x=10, y=0)

        self.table_frame = Frame(parent, bg="#535c68")
        self.table_frame.place(x=20, y=430, width=1490, height=140)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tree = ttk.Treeview(self.table_frame, columns=("SuspectID", "CaseID", "SuspectName", "Age", "Gender", "Address"), style="mystyle.Treeview", show='headings')

        self.tree.heading("SuspectID", text="SuspectID")
        self.tree.heading("CaseID", text="CaseID")
        self.tree.heading("SuspectName", text="SuspectName")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Address", text="Address")
        self.tree.column("SuspectID", width=100, anchor='center')
        self.tree.column("CaseID", width=100, anchor='center')
        self.tree.column("SuspectName", width=200, anchor='center')
        self.tree.column("Age", width=50, anchor='center')
        self.tree.column("Gender", width=100, anchor='center')
        self.tree.column("Address", width=300, anchor='center')
        self.tree.pack(fill=BOTH, expand=1)

    def fetch_and_display_suspect_details(self, case_id):
        if case_id:
            suspect_details = self.suspect_fetch_instance.fetch(case_id)
            if suspect_details:
                self.tree.delete(*self.tree.get_children())
                for suspect in suspect_details:
                    self.tree.insert("", "end", values=suspect)
            else:
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", "end", values=("No suspects.",))


class WitnessDetailsView:
    def __init__(self, parent, connection):
        self.witness_fetch_instance = Witness_fetch_one(connection)

        self.Witness_name_frame = Frame(parent, bg="#535c68")
        self.Witness_name_frame.place(x=20, y=570, width=1490, height=50)

        self.title = Label(self.Witness_name_frame, text="Witness List", font=("Calibri", 26, "bold"), bg="#535c68", fg="white")
        self.title.place(x=10, y=0)

        self.table_frame = Frame(parent, bg="#535c68")
        self.table_frame.place(x=20, y=620, width=1490, height=140)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=35)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))

        self.tree = ttk.Treeview(self.table_frame,columns=("WitnessID", "CaseID", "WitnessName", "Address", "PhoneNumber", "Statement"), style="mystyle.Treeview", show='headings')

        self.tree.heading("WitnessID", text="WitnessID")
        self.tree.heading("CaseID", text="CaseID")
        self.tree.heading("WitnessName", text="WitnessName")
        self.tree.heading("Address", text="Address")
        self.tree.heading("PhoneNumber", text="PhoneNumber")
        self.tree.heading("Statement", text="Statement")
        self.tree.column("WitnessID", width=100, anchor='center')
        self.tree.column("CaseID", width=100, anchor='center')
        self.tree.column("WitnessName", width=200, anchor='center')
        self.tree.column("Address", width=300, anchor='center')
        self.tree.column("PhoneNumber", width=150, anchor='center')
        self.tree.column("Statement", width=400, anchor='center')
        self.tree.pack(fill=BOTH, expand=1)

    def fetch_and_display_witness_details(self, case_id):
        if case_id:
            witness_details = self.witness_fetch_instance.fetch(case_id)
            if witness_details:
                self.tree.delete(*self.tree.get_children())
                for witness in witness_details:
                    self.tree.insert("", "end", values=witness)
            else:
                self.tree.delete(*self.tree.get_children())
                self.tree.insert("", "end", values=("No witnesses.",))


class MainApplication1:
    def __init__(self, start, back_callback):
        self.root1 = start
        self.back_callback = back_callback

        self.root1.geometry("1500x900")
        self.root1.title("Particular Case Details",)
        self.root1.state("zoomed")
        self.root1.configure(bg='#2a2e34')


        self.case_details_view = CaseDetailsView(self.root1, con)
        self.evidence_details_view = EvidenceDetailsView(self.root1, con)
        self.suspect_details_view = SuspectDetailsView(self.root1, con)
        self.witness_details_view = WitnessDetailsView(self.root1, con)

        self.create_widgets()

    def create_widgets(self):

        self.title = Label(self.root1, text="Forensic Management System", font=("Calibri", 26, "bold"),bg="#2a2e34", fg="white", pady=10)
        self.title.place(x=150, y=0)

        self.case_select_id = Label(self.root1, text="Case ID", font=("Calibri", 20), bg="#2a2e34", fg="white")
        self.case_select_id.place(x=870, y=15)
        self.txtcase_select_id = Entry(self.root1, font=("Calibri", 18), width=20)
        self.txtcase_select_id.place(x=980, y=15, width=300, height=40)

        self.btn_fetch = Button(self.root1, text="Fetch Details", font=("Calibri", 20, "bold"), fg="white", bg="#16a085", bd=0, pady=3, padx=20,command=self.fetch_and_display_details)
        self.btn_fetch.place(x=1300, y=15, height=40)

        self.btn_back = Button(self.root1, text="Back", font=("Calibri", 20, "bold"), fg="white", bg="green",
                               bd=0, pady=3, padx=20,  command=self.back_to_main)
        self.btn_back.place(x=20, y=15, height=40)

    def back_to_main(self):
        self.back_callback()

    def update_case_details(self, case_id):
        cursor = con.cursor()
        try:
            # Define the new details here
            # For example:
            new_case_name = "Updated Case Name"
            new_lead_investigator = "Updated Investigator"
            new_status = "Updated Status"
            new_date_opened = "2024-07-21"
            new_date_closed = None

            # Update the case details
            sql = """
                UPDATE cas_e
                SET CaseName = %s,
                    LeadInvestigator = %s,
                    Status = %s,
                    DateOpened = %s,
                    DateClosed = %s
                WHERE CaseID = %s
            """
            cursor.execute(sql, (
            new_case_name, new_lead_investigator, new_status, new_date_opened, new_date_closed, case_id))

            # Commit the changes
            con.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            con.rollback()

        finally:
            cursor.close()

    def fetch_and_display_details(self):
        case_id = self.txtcase_select_id.get()
        if case_id:
            # First, update the case details
            self.update_case_details(case_id)

            # Then, fetch and display the updated details
            self.case_details_view.fetch_and_display_case_details(case_id)
            self.evidence_details_view.fetch_and_display_evidence_details(case_id)
            self.suspect_details_view.fetch_and_display_suspect_details(case_id)
            self.witness_details_view.fetch_and_display_witness_details(case_id)

    def delete_case(self):
        case_id = self.txtcase_select_id.get()
        if case_id:
            self.delete_instance.delete_case(case_id)
            self.fetch_and_display_details()  # Refresh the display
            Case_g.displayAll(self)


# if __name__ == "__main__":
#     root = Tk()
#     app = MainApplication1(root, None)
#     root.mainloop()
