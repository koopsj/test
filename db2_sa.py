import ibm_db
import ibm_db_dbi
import pandas as pd
from sqlalchemy import create_engine

e = create_engine("db2+ibm_db://db2inst1:password@localhost:50000/sample")


sql = 'select tabschema, tabname from syscat.tables limit 10'
df = pd.read_sql_query(sql, e)
df.head(5)
print(df.to_json(orient="records"))
