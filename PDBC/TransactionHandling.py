from dbConnection import getConnection
conn=getConnection("student_details")
csr=conn.cursor()

try:
    conn.autocommit=False
    qry="Insert into MarksheetTable values(%s,%s,%s,%s,%s);"
    csr.execute(qry,(5,"Anshu",56,57,58))
    # csr.execute(qry,(5,"Pritesh",70,69,68))   #Primary key Duplicate Error
    csr.execute(qry,(6,"Pritesh",70,69,68))
    conn.commit()
    print("Transaction done Successfully")
except Exception as e:
    conn.rollback()
    print("Transaction Failed",e)
finally:
    csr.close()
    conn.close()
    print("Resources Closed")