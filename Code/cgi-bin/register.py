#!/usr/bin/python

import cgi
import cgitb
import MySQLdb as mariadb
import os

print "Content-type:text/html"
cgitb.enable()
x=cgi.FieldStorage()
fname=x.getvalue('fname')
uid=x.getvalue('uid')
pass1=x.getvalue('pass1')
pass2=x.getvalue('pass2')
dd=x.getvalue('dd')
mm=x.getvalue('mm')
yy=x.getvalue('yy')
gen=x.getvalue('gen')
ctc=x.getvalue('ctc')
fileitem=x['pic']

fname=cgi.escape(fname)
uid=cgi.escape(uid)
pass1=cgi.escape(pass1)
pass2=cgi.escape(pass2)
dd=cgi.escape(dd)
mm=cgi.escape(mm)
yy=cgi.escape(yy)
gen=cgi.escape(gen)
ctc=cgi.escape(ctc)

if(pass1 != pass2):
	print "location:http://192.168.43.63/cgi-bin/reg.py?q=perror"
	print ""
if((fname=="")| (uid=="")| (pass1=="")| (pass2=="")| (dd=="")| (mm=="")| (yy=="")| (gen=="")| (ctc=="")):
	print "location:http://192.168.43.63/cgi-bin/reg.py?q=ferror"
	print ""
if((len(fname)>30)| (len(uid)>30)| (len(pass1)<6)| (len(pass1)>30)| (len(pass2)<6)| (len(pass2)>30)| (len(ctc)>11)):
	print "location:http://192.168.0.8/cgi-bin/reg.py?q=ferror"
	print ""

if fileitem.filename:
	f = os.path.basename(uid)
        open('../html/pic/' + f, 'wb').write(fileitem.file.read())
else:
   os.system("sudo cp ../html/backgrounds/default.png ../html/pic/"+uid)

a=[]
flag=0

mariadb_connection=mariadb.connect(user='hadoop')
cursor=mariadb_connection.cursor()
cursor.execute("use hs")
cursor.execute("select USERNAME from USERS")
mariadb_connection.commit()
for USERNAME in cursor:
	a=USERNAME
	if(a[0] == uid):
		flag=1;
		break;

if (flag==1):
	mariadb_connection.close()
	print "location:http://192.168.43.63/cgi-bin/reg.py?q=merror"
	print ""
else:
	os.system("sudo mkdir ../html/IP/"+uid)
	os.system("sudo chmod 777 ../html/IP/"+uid)
	os.system("sudo mkdir ../html/file/"+uid)
	os.system("sudo chmod 777 ../html/file/"+uid)
	os.system("sudo chmod 777 ../html/pic/"+uid)
	dd=str(dd)
	mm=str(mm)
	yy=str(yy)
	cursor.execute("insert into USERS(USERNAME,PASSWORD,FULLNAME,DOB,GENDER,PHONE) values(%s,%s,%s,%s,%s,%s)",(uid,pass1,fname,dd+ "-"+mm+ "-"+yy,gen,ctc))
	mariadb_connection.commit()
	cursor.execute("create table "+uid+ "(DATANODE char(15) NOT NULL)")
	mariadb_connection.commit()
	mariadb_connection.close()
	print "location:http://192.168.43.63/cgi-bin/index.py?q=regsucess"	
	print ""
