from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()

qry="select * from MarksheetTable order by Maths desc"
# Get Top 3 Data
csr.execute(qry)
rows=csr.fetchmany(3)
print(rows)

print("Roll No\tName\tPhysics\tChemistry\tMaths")
print("------------------------------------------")
for row in rows:
    print("{}\t{}\t{}\t{}\t\t{}".format(row[0], row[1], row[2], row[3], row[4]))
    print("-------------------------------------------")

csr.close()
conn.close()