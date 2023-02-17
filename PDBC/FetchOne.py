# Fetch One Data:-
# from dbConnection import getConnection
# conn=getConnection("student_details")
# csr=conn.cursor()

# Roll_No=input("Enter the Roll No : ")
# qry="select * from MarksheetTable where Roll_No=%s"  #fetch one data through Roll no

# record=(Roll_No)
# csr.execute(qry)
# result=csr.fetchone()
# print("{}\t{}\t{}\t{}\t{}".format(result[0],result[1],result[2],result[3],result[4]))

# Fetch one asccending data or desccending data
from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()

qry="select * from MarksheetTable order by maths "    #asccending by default
csr.execute(qry)
result=csr.fetchone()
# print(result)     #return data in tuple
print("{}\t{}\t{}\t{}\t{}".format(result[0],result[1],result[2],result[3],result[4])) #without tuple

csr.close()
conn.close()