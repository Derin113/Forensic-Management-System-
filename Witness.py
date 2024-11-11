import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="fms"
)

class Witness:
    def __init__(self, connection):
        self.con = connection

    def add(self, WitnessID, CaseID, WitnessName, ContactInfo, Statement):
        res = self.con.cursor()
        sql = "INSERT INTO Witness (WitnessID, CaseID, WitnessName, ContactInfo, Statement) VALUES (%s, %s, %s, %s, %s)"
        params = (WitnessID, CaseID, WitnessName, ContactInfo, Statement)
        res.execute(sql, params)
        self.con.commit()

    def update(self, WitnessID, CaseID, WitnessName, ContactInfo, Statement):
        res = self.con.cursor()
        sql = "UPDATE Witness SET CaseID=%s, WitnessName=%s, ContactInfo=%s, Statement=%s WHERE WitnessID=%s"
        params = (CaseID, WitnessName, ContactInfo, Statement, WitnessID)
        res.execute(sql, params)
        self.con.commit()

    def delete(self, WitnessID):
        res = self.con.cursor()
        sql = "DELETE FROM Witness WHERE WitnessID = %s"
        params = (WitnessID,)
        res.execute(sql, params)
        self.con.commit()

    def fetch(self):
        res = self.con.cursor()
        sql = "SELECT * FROM Witness"
        res.execute(sql)
        result = res.fetchall()
        return result
