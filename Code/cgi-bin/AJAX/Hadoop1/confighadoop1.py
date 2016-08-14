#!/usr/bin/python

import cgi
import commands
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""
flag=1
nn=[]
sn=[]
jt=[]
try:
	mariadb_connection=mariadb.connect(user='hadoop')
	cursor=mariadb_connection.cursor()
	cursor.execute("use hs")
	cursor.execute("select NAMENODE from CLUSTER where USERNAME=%s",(uid))
	mariadb_connection.commit()
	for NAMENODE in cursor:
		a=NAMENODE
		nn=a[0]
	cursor.execute("select SNAMENODE from CLUSTER where USERNAME=%s",(uid))
	mariadb_connection.commit()
	for SNAMENODE in cursor:
		a=SNAMENODE
		sn=a[0]
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
	exp="<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n</configuration>"
	core=exp.replace('<configuration>','<configuration>\n<property>\n<name>fs.default.name</name>\n<value></value>\n</property>')
	core=core.replace('<value>','<value>hdfs://'+nn+ ':10001')
	f1=open('/var/www/html/IP/'+uid+ '/core-site.xml','w')
	f1.write(core)
	f1.close()
	hdfsnn=exp.replace('<configuration>','<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/namenode</value>\n</property>')
	f1=open('/var/www/html/IP/'+uid+ '/hdfsnn.xml','w')
	f1.write(hdfsnn)
	f1.close()
	hdfssn=exp.replace('<configuration>','<configuration>\n<property>\n<name>dfs.http.address</name>\n<value>:50070</value>\n</property>\n<property>\n<name>dfs.secondary.http.address</name>\n<value>:50090</value>\n</property>\n<property>\n<name>fs.checkpoint.dir</name>\n<value>/namenode</value>\n</property>\n<property>\n<name>fs.checkpoint.period</name>\n<value>60</value>\n</property>')
	hdfssn=hdfssn.replace('<value>:50070','<value>'+nn+ ':50070')
	hdfssn=hdfssn.replace('<value>:50090','<value>'+sn+ ':50090')
	f1=open('/var/www/html/IP/'+uid+ '/hdfssn.xml','w')
	f1.write(hdfssn)
	f1.close()
	hdfs=exp.replace('<configuration>','<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/datanode</value>\n</property>')
	f1=open('/var/www/html/IP/'+uid+ '/hdfs-site.xml','w')
	f1.write(hdfs)
	f1.close()
	mapred=exp.replace('<configuration>','<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value></value>\n</property>')
	mapred=mapred.replace('<value>','<value>'+jt+ ':9001')
	f1=open('/var/www/html/IP/'+uid+ '/mapred-site.xml','w')
	f1.write(mapred)
	f1.close()
	a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'rm -rf /etc/hadoop/core-site.xml /etc/hadoop/hdfs-site.xml /etc/hadoop/mapred-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
	if(a ==""):
		print "OK"
	else:
		print "The Ip Listed Below Are Not Reachable "+a
