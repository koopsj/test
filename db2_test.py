import ibm_db
 #For connecting to local database named pydev for user db2inst1 and password secret, use below example
 #ibm_db_conn = ibm_db.connect('pydev', 'db2inst1', 'secret')
 #For connecting to remote database named pydev for uid db2inst and pwd secret on host host.test.com, use below example
 # Connect using ibm_db
conn_str='database=testdb;hostname=localhost;port=50000;protocol=tcpip;uid=db2inst1;pwd=password'
ibm_db_conn = ibm_db.connect(conn_str,'','')

 # Connect using ibm_db_dbi
import ibm_db_dbi
conn = ibm_db_dbi.Connection(ibm_db_conn)
# Drop table
drop_tab="drop table if exists mytable"
ibm_db.exec_immediate(ibm_db_conn, drop_tab)
# create table using ibm_db
create="create table mytable(id int, name varchar(50))"
ibm_db.exec_immediate(ibm_db_conn, create)

 # Execute tables API
conn.tables('DB2INST1', '%')
[{'TABLE_CAT': None, 'TABLE_SCHEM': 'DB2INST1', 'TABLE_NAME': 'MYTABLE', 'TABLE_TYPE': 'TABLE', 'REMARKS': None}]

 # Insert 3 rows into the table
insert = "insert into mytable values(?,?)"
params=((1,'Sanders'),(2,'Pernal'),(3,'OBrien'))
stmt_insert = ibm_db.prepare(ibm_db_conn, insert)
ibm_db.execute_many(stmt_insert,params)

 # Fetch data using ibm_db_dbi
select="select id, name from mytable"
cur = conn.cursor()
cur.execute(select)
row=cur.fetchall()
print("{} \t {} \t {}".format(row[0],row[1],row[2]),end="\n")
row=cur.fetchall()
print(row)

 # Fetch data using ibm_db
stmt_select = ibm_db.exec_immediate(ibm_db_conn, select)
cols = ibm_db.fetch_tuple( stmt_select )
print("%s, %s" % (cols[0], cols[1]))
cols = ibm_db.fetch_tuple( stmt_select )
print("%s, %s" % (cols[0], cols[1]))
cols = ibm_db.fetch_tuple( stmt_select )
print("%s, %s" % (cols[0], cols[1]))
cols = ibm_db.fetch_tuple( stmt_select )
print(cols)

 # Close connections
cur.close()
 # Dropping the table created
drop = "drop table mytable"
stmt_delete = ibm_db.exec_immediate(ibm_db_conn,drop)
conn.tables('DB2INST1','MY%')

ibm_db.close(ibm_db_conn)

