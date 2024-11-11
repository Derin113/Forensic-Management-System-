import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="12345", database="fms")

class Evidence:
    def __init__(self,connection):
        self.con = connection

    def add(self,EvidenceID,CaseID,DateCollected,CollectedBy,StorageLocation,Location,EvidenceType,Description):
        res = self.con.cursor()
        sql = "insert into Evidence (EvidenceID,CaseID,DateCollected,CollectedBy,StorageLocation,Location,EvidenceType,Description) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        user = (EvidenceID, CaseID, DateCollected, CollectedBy, StorageLocation, Location, EvidenceType, Description)
        res.execute(sql,user)
        self.con.commit()

    def update(self,EvidenceID,CaseID,DateCollected,CollectedBy,StorageLocation,Location,EvidenceType,Description):
        res = self.con.cursor()
        sql = "update Evidence set CaseID=%s,DateCollected=%s,CollectedBy=%s,StorageLocation=%s,Location=%s,EvidenceType=%s,Description=%s where EvidenceID=%s"
        user = (CaseID,DateCollected,CollectedBy,StorageLocation,Location,EvidenceType,Description,EvidenceID)
        res.execute(sql,user)
        self.con.commit()

    def delete(self,EvidenceID):
        res = self.con.cursor()
        sql = "delete from Evidence where EvidenceID = %s"
        user = (EvidenceID,)
        res.execute(sql,user)
        self.con.commit()

    def fetch(self):
        res = self.con.cursor()
        sql = "select * from Evidence"
        res.execute(sql)
        result = res.fetchall()
        return result
