#!/usr/bin/python

import cgi
import Cookie
import random
import datetime
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
pass1=x.getvalue('pass1')
uid=cgi.escape(uid)
pass1=cgi.escape(pass1)

if ((uid=="") | (pass1=="")):
	print "location:http://192.168.43.63/cgi-bin/index.py?q=ferror"
	print ""
elif ((len(uid)>30)| (len(pass1)<6)| (len(pass1)>30)):
	print "location:http://192.168.43.63/cgi-bin/index.py?q=ferror"
	print ""
else:
	a=[]
	b=[]
	flag=1
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select USERNAME from USERS")
	mariadb_connection.commit()
	for USERNAME in cursor:
		a=USERNAME
		if(a[0]==uid):
			cursor.execute("select PASSWORD from USERS where USERNAME=%s",(uid))
			mariadb_connection.commit()
			for PASSWORD in cursor:
				b=PASSWORD
				if(b[0]==pass1):
					flag=0
					break;
						
	if(flag==1):
		mariadb_connection.close()
		print "location:http://192.168.43.63/cgi-bin/index.py?q=merror"
		print ""
	else:
		z=random.randint(0,1000000000)
		future=datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=1)
		cursor.execute("select USERNAME from COOKIE where USERNAME=%s",(uid))
		mariadb_connection.commit()
		for USERNAME in cursor:
			a=USERNAME
			if(a[0] == uid):
				flag=1
				break;
		
		if(flag==1):
			cursor.execute("update COOKIE set CNO=%s ,AUTOLOGOUT=%s where USERNAME=%s",(z,future,uid))
			mariadb_connection.commit()
		else:		
			cursor.execute("insert into COOKIE(CNO,USERNAME,PASSWORD,AUTOLOGOUT) values(%s,%s,%s,%s)",(z,uid,pass1,future))
			mariadb_connection.commit()
		mariadb_connection.close()
		cookie=Cookie.SimpleCookie()
		cookie['Ha2uPSoLuTiOns']=z
		print cookie
		print "location:http://192.168.43.63/cgi-bin/services.py"
		print ""
