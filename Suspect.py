import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="12345", database="fms")

class Suspect:
    def __init__(self, connection):
        self.con = connection

    def add(self, SuspectID, CaseID, SuspectName, Age, Gender, Address):
        res = self.con.cursor()
        sql = "INSERT INTO Suspect (SuspectID, CaseID, SuspectName, Age, Gender, Address) VALUES (%s, %s, %s, %s, %s, %s)"
        user = (SuspectID, CaseID, SuspectName, Age, Gender, Address)
        res.execute(sql, user)
        self.con.commit()

    def update(self, SuspectID, CaseID, SuspectName, Age, Gender, Address):
        res = self.con.cursor()
        sql = "UPDATE Suspect SET CaseID=%s, SuspectName=%s, Age=%s, Gender=%s, Address=%s WHERE SuspectID=%s"
        user = (CaseID, SuspectName, Age, Gender, Address, SuspectID)
        res.execute(sql, user)
        self.con.commit()

    def delete(self, SuspectID):
        res = self.con.cursor()
        sql = "DELETE FROM Suspect WHERE SuspectID = %s"
        user = (SuspectID,)
        res.execute(sql, user)
        self.con.commit()

    def fetch(self):
        res = self.con.cursor()
        sql = "SELECT * FROM Suspect"
        res.execute(sql)
        result = res.fetchall()
        return result
