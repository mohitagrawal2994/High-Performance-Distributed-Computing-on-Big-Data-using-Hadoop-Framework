#!/usr/bin/python

import os
import Cookie
import datetime
import MySQLdb as mariadb

print "Content-type:text/html"
a=[]
flag=1
f=datetime.datetime.now().replace(microsecond=0)
try:
	cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	b=cookie["Ha2uPSoLuTiOns"].value
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select AUTOLOGOUT from COOKIE")
	mariadb_connection.commit()
	for AUTOLOGOUT in cursor:
		a=AUTOLOGOUT
		if(a[0] < f):
			cursor.execute("delete from COOKIE where AUTOLOGOUT=%s",(a[0]))
			mariadb_connection.commit()
			
	cursor.execute("select CNO from COOKIE")
	mariadb_connection.commit()
	for CNO in cursor:
		a=CNO
		if(a[0] == b):
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(a[0]))
			for USERNAME in cursor:
				a=USERNAME
				cursor.execute("delete from USERS where USERNAME=%s",(a[0]))
				mariadb_connection.commit()
				cursor.execute("delete from CLUSTER where USERNAME=%s",(a[0]))
				mariadb_connection.commit()
				cursor.execute("drop table "+a[0])
				mariadb_connection.commit()
				os.system("sudo rm -rf ../html/IP/"+a[0])
				os.system("sudo rm -rf ../html/file/"+a[0])
				os.system("sudo rm -f ../html/pic/"+a[0])
				mariadb_connection.commit()
				cursor.execute("delete from COOKIE where CNO=%s",(b))
				mariadb_connection.commit()
				flag=0

except:
	flag=1

if(flag==1):
	print "location:http://192.168.43.63/cgi-bin/index.py?q=merror"
	print ""
else:
	print "location:http://192.168.43.63/cgi-bin/index.py?q=accsucess"
	print ""
