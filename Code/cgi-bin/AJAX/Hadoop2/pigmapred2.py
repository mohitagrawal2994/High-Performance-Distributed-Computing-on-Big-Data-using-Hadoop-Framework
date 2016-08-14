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
	exp='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!--\n  Licensed under the Apache License, Version 2.0 (the "License");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an "AS IS" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License. See accompanying LICENSE file.\n-->\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapreduce.framework.name</name>\n<value>yarn</value>\n</property>\n<property>\n<name>mapreduce.jobhistory.address</name>\n<value>:10020</value>\n</property>\n</configuration>\n'
	mapred=exp.replace('<value>:10020','<value>'+jt+ ':10020')
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


