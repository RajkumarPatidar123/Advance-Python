from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()
csr.callproc("getAllData")
result=csr.fetchall()
# for row in result:        #get each tuple in new line
#     print(row)
#     print("------------------------------")
print("Id\tCity\t\tCapacity")
print("-------------------------------------------")
for row in result:                # Get value without tuple
    print("{}\t{}\t{}".format(row[0],row[1],row[2]))
    print("-------------------------------------------")

csr.close()
conn.close()