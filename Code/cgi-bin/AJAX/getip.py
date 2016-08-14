#!/usr/bin/python

import commands
import Cookie
import os
import MySQLdb as mariadb

print "Content-type:text/html"
print ""
flag=1
try:
	a=[]
	cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	b=cookie["Ha2uPSoLuTiOns"].value
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select CNO from COOKIE")
	mariadb_connection.commit()
	for CNO in cursor:
		a=CNO
		if(a[0] == b):
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(b))
			mariadb_connection.commit()
			for USERNAME in cursor:
				a=USERNAME
				uid=a[0]
				flag=0
	
			a=commands.getoutput("sudo nmap -sP 192.168.43.2-254 --exclude 192.168.43.180,192.168.43.63 -n | grep 'Nmap scan' | awk '{print $5}'")
			f1=open('/var/www/html/IP/'+uid+ '/IPR.txt','w')
			f1.write(a)
			f1.close()
except:
	flag=1

if(flag ==1):
	print "Error"
else:
	print "OK"
