# Q. Delete the Record through Roll No Using PDBC ?

from dbConnection import getConnection
connection=getConnection("student_details")
csr=connection.cursor()

Roll_No=input("Enter Roll No to Delete a Record:\n ")

qry="Delete from MarksheetTable where Roll_No=%s"
Record=(Roll_No)
csr.execute(qry,Record)
connection.commit()
print("Record Deleted")