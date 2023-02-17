# import the module
import pymysql

# create a connection object
connection=pymysql.connect(
    host="localhost",  #ip address
    port=3306,
    user="root",
    password="root",
    database="student_details"
)
# create a cursor object
csr=connection.cursor()

# create a query
qry="""create table MarksheetTable
    (Roll_no int primary key,
    Name varchar(25),
    Physics int,
    Chemistry int,
    Maths int)"""

# Execute the query
csr.execute(qry)
print("Table Created") 