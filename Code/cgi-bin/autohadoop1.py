#!/usr/bin/python

import os
import cgi
import Cookie
import commands
import datetime
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
hd=x.getvalue('hd')
hd=cgi.escape(hd)
h=x.getvalue('hive')
p=x.getvalue('pig')
s=x.getvalue('splunk')

if h:
	hive="Y"
else:
	h="0"
	hive="N"
if p:
	pig="Y"
else:
	p="0"
	pig="N"
if s:
	splunk="Y"
else:
	s="0"
	splunk="N"


a=[]
flag=1
f=datetime.datetime.now().replace(microsecond=0)
future=datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=1)
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
			cursor.execute("update COOKIE set AUTOLOGOUT=%s where CNO=%s",(future,a[0]))
			mariadb_connection.commit()
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(a[0]))
			mariadb_connection.commit()
			for USERNAME in cursor:
				a=USERNAME
				uid=a[0]
				cursor.execute("select FULLNAME from USERS where USERNAME=%s",(a[0]))
				mariadb_connection.commit()
				for FULLNAME in cursor:
					a=FULLNAME
					name=a[0]
					flag=0
				cursor.execute("select PASSWORD from COOKIE where CNO=%s",(b))
				mariadb_connection.commit()
				for PASSWORD in cursor:
					a=PASSWORD
					pass1=a[0]
					flag=0	
							
		else:
			flag=1
except:
	flag=1

if(flag==1):
	print "location:http://192.168.43.63/cgi-bin/index.py?q=merror"
	print ""
else:
	f=open('/var/www/html/IP/'+uid+ '/IPR.txt','r')
	a=f.read()
	f.close()
	b=a.split("\n")
	c=len(b)
	f1=open('/var/www/html/IP/'+uid+ '/ans.txt','w')
	f1.write("[cli]\n")
	f1.write(b[0])
	f1.write("\t")
	f1.write("ansible_ssh_user=root\t")
	f1.write("ansible_ssh_pass="+pass1+ " \n")
	f1.write("[nn]\n")
	f1.write(b[1])
	f1.write("\t")
	f1.write("ansible_ssh_user=root\t")
	f1.write("ansible_ssh_pass="+pass1+ " \n")
	f1.write("[sn]\n")
	f1.write(b[2])
	f1.write("\t")
	f1.write("ansible_ssh_user=root\t")
	f1.write("ansible_ssh_pass="+pass1+ " \n")
	f1.write("[bn]\n")
	f1.write(b[3])
	f1.write("\t")
	f1.write("ansible_ssh_user=root\t")
	f1.write("ansible_ssh_pass="+pass1+ " \n")
	f1.write("[jt]\n")
	f1.write(b[4])
	f1.write("\t")
	f1.write("ansible_ssh_user=root\t")
	f1.write("ansible_ssh_pass="+pass1+ " \n")
	f1.write("[dn]\n")
	for i in range(5,c):
		f1.write(b[i])
		f1.write("\t")
		f1.write("ansible_ssh_user=root\t")
		f1.write("ansible_ssh_pass="+pass1+ " \n")
		cursor.execute("insert into "+uid+ "(DATANODE) values(%s)",(b[i]))
		mariadb_connection.commit()	
	
	f1.close()
	cursor.execute("insert into CLUSTER(USERNAME,HADOOPV,HIVE,PIG,SPLUNK,CLIENT,NAMENODE,SNAMENODE,BNAMENODE,JOBTRACKER) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(uid,hd,hive,pig,splunk,b[0],b[1],b[2],b[3],b[4]));
	mariadb_connection.commit()
	a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/repo/hadoop.repo dest=/etc/yum.repos.d/hadoop.repo' | grep 'UNREACHABLE' | awk '{print $1}'")
	if( a == "" ):
		if(hd == "1"):
			print "location:http://192.168.43.63/cgi-bin/mancluster1.py?w=1&h="+h+ "&p="+p+ "&s="+s
			print ""
		else:
			print "location:http://192.168.43.63/cgi-bin/mancluster1.py?w=2&h="+h+ "&p="+p+ "&s="+s
			print ""
	else:
		print "location:http://192.168.43.63/cgi-bin/autohadoop.py?q=ipuerror&w="+a
		print ""
	
