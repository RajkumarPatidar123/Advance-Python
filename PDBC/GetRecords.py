# Get all Record:-
from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()
qry="select * from MarksheetTable;"
csr.execute(qry)
resultset=csr.fetchall()
print(resultset)            #get All tuple(Nested Tuple) in 1 line
print("-----------------------------------------------")
for row in resultset:       #get each tuple in new line
    print(row)
    print("----------------------------------------------")

print("------------------------------------------------Particular Value(without tuple)------")
print("Roll No\tName\tPhysics\tChemistry\tMaths")
for row in resultset:
    print("{}\t{}\t {}\t {}\t\t{}".format(row[0],row[1],row[2],row[3],row[4]))
    print("--------------------------------------------------")


csr.close
conn.close

# Task:-
# Q. Get the Record through Roll No Using PDBC ?

# from dbConnection import getConnection
# conn=getConnection("student_details")
# csr=conn.cursor()
# Roll_No=input("Enter Roll No : ")
# qry="select * from student_table where Roll_No=%s"
# result=(Roll_No)
# csr.execute(qry,result)

# resultset=csr.fetchall()
# print(resultset)