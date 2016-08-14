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
	exp='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!--\n  Licensed under the Apache License, Version 2.0 (the "License");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an "AS IS" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License. See accompanying LICENSE file.\n-->\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n</configuration>\n'
	core=exp.replace('<configuration>','<configuration>\n<property>\n<name>fs.default.name</name>\n<value></value>\n</property>')
	core=core.replace('<value>','<value>hdfs://'+nn+ ':10001')
	f1=open('/var/www/html/IP/'+uid+ '/core-site.xml','w')
	f1.write(core)
	f1.close()
	hdfsnn=exp.replace('<configuration>','<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>file:/data/namenode</value>\n</property>')
	f1=open('/var/www/html/IP/'+uid+ '/hdfsnn.xml','w')
	f1.write(hdfsnn)
	f1.close()
	hdfssn=exp.replace('<configuration>','<configuration>\n<property>\n<name>dfs.http.address</name>\n<value>:50070</value>\n</property>\n<property>\n<name>dfs.secondary.http.address</name>\n<value>:50090</value>\n</property>\n<property>\n<name>fs.checkpoint.dir</name>\n<value>/namenode</value>\n</property>\n<property>\n<name>fs.checkpoint.period</name>\n<value>60</value>\n</property>')
	hdfssn=hdfssn.replace('<value>:50070','<value>'+nn+ ':50070')
	hdfssn=hdfssn.replace('<value>:50090','<value>'+sn+ ':50090')
	f1=open('/var/www/html/IP/'+uid+ '/hdfssn.xml','w')
	f1.write(hdfssn)
	f1.close()
	hdfs=exp.replace('<configuration>','<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>file:/data/datanode</value>\n</property>')
	f1=open('/var/www/html/IP/'+uid+ '/hdfs-site.xml','w')
	f1.write(hdfs)
	f1.close()
	exp='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!--\n  Licensed under the Apache License, Version 2.0 (the "License");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an "AS IS" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License. See accompanying LICENSE file.\n-->\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n\n</configuration>\n'
	mapred=exp.replace('<configuration>','<configuration>\n<property>\n<name>mapreduce.framework.name</name>\n<value>yarn</value>\n</property>')
	f1=open('/var/www/html/IP/'+uid+ '/mapred-site.xml','w')
	f1.write(mapred)
	f1.close()
	exp='<?xml version="1.0"?>\n<!--\n  Licensed under the Apache License, Version 2.0 (the "License");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an "AS IS" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License. See accompanying LICENSE file.\n-->\n<configuration>\n\n<!-- Site specific YARN configuration properties -->\n\n</configuration>\n'
	yarncli=exp.replace('<configuration>','<configuration>\n<property>\n<name>yarn.resourcemanager.resource-tracker.address</name>\n<value>:8025</value>\n</property>\n<property>\n<name>yarn.resourcemanager.scheduler.address</name>\n<value>:8030</value>\n</property>\n<property>\n<name>yarn.resourcemanager.address</name>\n<value>:8032</value>\n</property>')
	yarncli=yarncli.replace('<value>','<value>'+jt)
	f1=open('/var/www/html/IP/'+uid+ '/yarncli.xml','w')
	f1.write(yarncli)
	f1.close()
	yarnrs=exp.replace('<configuration>','<configuration>\n<property>\n<name>yarn.resourcemanager.resource-tracker.address</name>\n<value>:8025</value>\n</property>\n<property>\n<name>yarn.resourcemanager.scheduler.address</name>\n<value>:8030</value>\n</property>')
	yarnrs=yarnrs.replace('<value>','<value>'+jt)
	f1=open('/var/www/html/IP/'+uid+ '/yarnrs.xml','w')
	f1.write(yarnrs)
	f1.close()
	yarn=exp.replace('<configuration>','<configuration>\n<property>\n<name>yarn.resourcemanager.aux-services</name>\n<value>mapreduce_shuffle</value>\n</property>\n<property>\n<name>yarn.resourcemanager.resource-tracker.address</name>\n<value>:8025</value>\n</property>')
	yarn=yarn.replace('<value>:8025','<value>'+jt+ ':8025')
	f1=open('/var/www/html/IP/'+uid+ '/yarn.xml','w')
	f1.write(yarn)
	f1.close()
	print "OK"
