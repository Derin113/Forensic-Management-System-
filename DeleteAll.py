import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="12345", database="fms")

class Delete:
    def __init__(self, connection):
        self.con = connection

    def delete_case(self, case_id):
        cursor = self.con.cursor()
        try:

            # Disable foreign key checks
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

            # Delete from all related tables
            cursor.execute("DELETE FROM witness WHERE CaseID = %s;", (case_id,))
            cursor.execute("DELETE FROM suspect WHERE CaseID = %s;", (case_id,))
            cursor.execute("DELETE FROM evidence WHERE CaseID = %s;", (case_id,))
            cursor.execute("DELETE FROM cas_e WHERE CaseID = %s;", (case_id,))

            # Commit the changes
            self.con.commit()

            # Enable foreign key checks
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.con.rollback()

        finally:
            cursor.close()

