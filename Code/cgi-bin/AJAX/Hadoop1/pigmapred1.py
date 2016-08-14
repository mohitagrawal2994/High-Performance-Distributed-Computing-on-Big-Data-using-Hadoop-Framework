#!/usr/bin/python

import cgi
import commands
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""
flag=1
jt=[]

try:
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select JOBTRACKER from CLUSTER where USERNAME=%s",(uid))
	mariadb_connection.commit()
	for JOBTRACKER in cursor:
		a=JOBTRACKER
		jt=a[0]
		flag=0
except:
	flag=1

if(flag==1):
	print "There was some error in Database"
else:
	exp="<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>:9001</value>\n</property>\n<property>\n<name>mapreduce.jobhistory.address</name>\n<value>:10020</value>\n</property>\n</configuration>\n"
	mapred=exp.replace('<value>','<value>'+jt)
	f1=open('/var/www/html/IP/'+uid+ '/mapred-site.xml','w')
	f1.write(mapred)
	f1.close()
	a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/mapred-site.xml dest=/etc/hadoop/mapred-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
	if(a == ""):
		a=commands.getoutput("sudo ansible jt -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop-daemon.sh start historyserver' | grep 'UNREACHABLE' | awk '{print $1}' " )
		if(a == ""):	
			print "OK"
		else:
			print "The Ip Listed Below Are Not Reachable "+a
	else:
		print "The Ip Listed Below Are Not Reachable "+a


