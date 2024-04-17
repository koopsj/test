# An object of Flask class is our WSGI application.
from flask import Flask
from flask import jsonify
import ibm_db
import ibm_db_dbi

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


cnxn = ibm_db.connect('DATABASE=sample;'
                'HOSTNAME=localhost;'
                'PORT=50000;'
                'PROTOCOL=TCPIP;'
                'UID=db2inst1;'
                'PWD=password;', '', '')

conn=ibm_db_dbi.Connection(cnxn)

# http://dksrv131:5000/list_users_by_proc
@app.route('/list_schema')
def list_users_by_proc():

	cur = conn.cursor()
	cur.execute('select tabschema from syscat.tables group by tabschema')
	rows  = cur.fetchall()
	cur.close()
	return jsonify(rows)


# http://dksrv131:5000/list_users_by_view
@app.route('/list_users_by_view')
def list_users_by_view():

	cur = conn.cursor()
	cur.execute('select * from microdemo.users_full')
	rows  = cur.fetchall()
	cur.close()
	return jsonify(rows)


# main driver function
if __name__ == '__main__':

	# the host='0.0.0.0' describes the interface - aka. "any"  interface
	app.run(host='192.168.0.43')
