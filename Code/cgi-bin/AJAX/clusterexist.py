#!/usr/bin/python

import cgi
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

a=[]
flag=1
try:
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select USERNAME from CLUSTER where USERNAME=%s",(uid))
	mariadb_connection.commit()
	for USERNAME in cursor:
		a=USERNAME
		if(a[0] == uid):
			flag=0
except:
	flag=1

if(flag==1):
	pass;
else:
	print "OK"
