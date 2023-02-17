from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()

Roll_No=input("Enter Roll No whose Name to Update : ")
Name=input("Enter Name to Update the Record Name : ")
qry="Update MarksheetTable set Name=%s where roll_no=%s"

record=(Name,Roll_No)

i=csr.execute(qry, record)
conn.commit()
print("Name Updated",i)