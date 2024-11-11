import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="12345", database="fms")

class Case:
    def __init__(self,connection):
        self.con = connection

    def add(self,CaseID,CaseName,LeadInvestigator,Status,DateOpened,DateClosed):
        res = self.con.cursor()
        sql = "insert into cas_e (CaseID,CaseName,LeadInvestigator,Status,DateOpened,DateClosed) values (%s,%s,%s,%s,%s,%s)"
        user = (CaseID,CaseName,LeadInvestigator,Status,DateOpened,DateClosed)
        res.execute(sql,user)
        self.con.commit()

    def update(self,CaseID,CaseName,LeadInvestigator,Status,DateOpened,DateClosed):
        res = self.con.cursor()
        sql = "update cas_e set CaseName=%s,LeadInvestigator=%s,Status=%s,DateOpened=%s,DateClosed=%s where CaseID=%s"
        user = (CaseName,LeadInvestigator,Status,DateOpened,DateClosed,CaseID)
        res.execute(sql,user)
        self.con.commit()

    def delete(self,CaseID):
        res = self.con.cursor()
        sql = "delete from cas_e where CaseID = %s"
        user = (CaseID,)
        res.execute(sql,user)
        self.con.commit()

    def fetch(self):
        res = self.con.cursor()
        con.commit()
        sql = "select * from cas_e"
        res.execute(sql)
        result = res.fetchall()
        return result
