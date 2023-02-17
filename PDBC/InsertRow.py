import pymysql
connection=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    db="student_details"
)
csr=connection.cursor()

qry="""insert into MarksheetTable values(1,"Raja",77,76,75);"""

i=csr.execute(qry)
connection.commit()  #make the changes in DB table(Data isike through database me jake save hoga)
print("Row Inserted",i)