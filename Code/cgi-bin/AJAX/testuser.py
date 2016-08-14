#!/usr/bin/python

import cgi
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
name=x.getvalue('q')
print ""

if (name == ""):
	print ""
else:
	a=[]
	flag=0
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select USERNAME from USERS")
	mariadb_connection.commit()
	for USERNAME in cursor:
		a=USERNAME;
		if(a[0] != name):
			flag=1;
		else:
			flag=0;
			break;
	
	mariadb_connection.close()
	if(flag==1):
		print "Not A Valid User"
	
