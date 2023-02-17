from dbConnection import getConnection
from MarksheetBean import Marksheet

class MarksheetDao:

    def Add(self,bean):
        if isinstance(bean,Marksheet):
            connection=getConnection("student_details")
            csr=connection.cursor()
            qry="Insert into MarksheetTable values(%s,%s,%s,%s,%s)"

            pk=MarksheetDao.NextPk(bean)
            #rn=bean.getRoll_no()
            n=bean.getName()
            p=bean.getPhysics()
            c=bean.getChemistry()
            m=bean.getMaths()
            i=csr.execute(qry,(pk,n,p,c,m))
            connection.commit()

            if i>0:
                print("Marksheet Added")
            else:
                print("Marksheet Not Added")


    def NextPk(self):
        pk=0
        conn=getConnection("student_details")
        csr=conn.cursor()
        qry="select max(Roll_no) from MarksheetTable"
        csr.execute(qry)
        result=csr.fetchall()
        conn.commit()
        csr.close()
        conn.close()

        for m in result:
            pk = m[0]
            return pk + 1    

    def Update(self,bean):
        if isinstance(bean,Marksheet):
            connection=getConnection("student_details")
            csr=connection.cursor()
            qry="update MarksheetTable set Name=%s where Roll_no=%s"

            rn=bean.getRoll_no()
            n=bean.getName()

            i=csr.execute(qry,(n,rn))
            connection.commit()

            if i>0:
                print("Marksheet Updated")
            else:
                print("Not Update")

    def Delete(self,bean):
        if isinstance(bean,Marksheet):
            conn=getConnection("student_details")
            csr=conn.cursor()
            qry="delete from MarksheetTable where roll_no=%s"
            rn=bean.getRoll_no()
            i=csr.execute(qry,(rn))
            conn.commit()

            if i>0:
                print("Record Deleted")
            else:
                print("Not Delete")

    def Get(self,bean):
        if isinstance(bean,Marksheet):
            conn=getConnection("student_details")
            csr=conn.cursor()
            qry="select * from MarksheetTable where roll_no=%s"
            rn=bean.getRoll_no()
            csr.execute(qry,(rn,))
            i=csr.fetchone()
            conn.commit()

            if i != None:
                print("Data Fetched",i)

    def getMeritList(self):
            conn=getConnection("student_details")
            csr=conn.cursor()
            qry="select Roll_no,Name,Physics,Chemistry,Maths,(Physics+Chemistry+Maths) as Total from MarksheetTable where Physics>=33 and Chemistry>=33 and Maths>=33 order by Total desc limit 5"
            csr.execute(qry)
            result=csr.fetchall()

            for i in result:
                print(i)

    def Search(self):
        conn=getConnection("student_details")
        csr=conn.cursor()
        qry="select * from MarksheetTable"
        csr.execute(qry)
        result=csr.fetchall()

        print("Roll No\tName\tPhysics\tChemistry\tMaths")
        print("----------------------------------------------")

        for row in result:
            print("{}\t{}\t{}\t{}\t\t{}".format(row[0], row[1], row[2], row[3], row[4]))
            print("----------------------------------------------")