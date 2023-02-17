from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()

Roll_No=input("Enter Roll No :\n")
Name=input("Enter Name :\n")
Phy=input("Enter Physics Score :\n")
Chem=input("Enter Chemistry Score :\n")
Maths=input("Enter Maths Score :\n")

qry="Insert into MarksheetTable values(%s,%s,%s,%s,%s)"

record=(Roll_No,Name,Phy,Chem,Maths)

i=csr.execute(qry,record)
conn.commit()
print("Marksheet Added",i)
