from dbConnection import getConnection
connection=getConnection("student_details")
csr=connection.cursor()
csr.execute("select * from unit")
csr.fetchall()
data=csr.description
print(data)
csr.close()
connection.close()