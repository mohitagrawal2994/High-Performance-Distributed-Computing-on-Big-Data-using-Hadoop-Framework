#!/usr/bin/python

import cgi
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
ctc=x.getvalue('ctc')
pass1=x.getvalue('pass1')
pass2=x.getvalue('pass2')

uid=cgi.escape(uid)
ctc=cgi.escape(ctc)
pass1=cgi.escape(pass1)
pass2=cgi.escape(pass2)

if( pass1 != pass2 ):
	print "location:http://192.168.43.63/cgi-bin/forg.py?q=perror"
	print ""

if((uid =="")| (ctc == "")| (pass1 == "")| (pass2 == "")):
	print "location:http://192.168.43.63/cgi-bin/forg.py?q=ferror"
	print ""
elif((len(uid) > 30)| (len(pass1)<6)| (len(pass2)<6)| (len(pass1)>30)| (len(pass1)>30)):
	print "location:http://192.168.43.63/cgi-bin/forg.py?q=ferror"
	print ""
else:
	a=[]
	b=[]
	flag=0
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select USERNAME from USERS")
	mariadb_connection.commit()
	for USERNAME in cursor:
		a=USERNAME
		if(a[0] == uid):
			cursor.execute("select PHONE from USERS where USERNAME=%s",(uid))
			mariadb_connection.commit()
			for CONTACT in cursor:
				b=CONTACT
				if(b[0] == ctc):
					flag=1;
					break;	
	if(flag==0):
		mariadb_connection.close()
		print "location:http://192.168.43.63/cgi-bin/forg.py?q=merror"
		print ""
	else:
		a=[]
		cursor.execute("update USERS set PASSWORD=%s where USERNAME=%s",(pass1,uid))
		mariadb_connection.commit()
		mariadb_connection.close()
		print "location:http://192.168.43.63/cgi-bin/index.py?q=forgsucess"
		print ""
		
