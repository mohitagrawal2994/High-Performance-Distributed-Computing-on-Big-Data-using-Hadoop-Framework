#!/usr/bin/python

import cgi
import commands
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

flag=1
a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/core-site.xml dest=/etc/hadoop/core-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
if(a == ""):
	a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/mapred-site.xml dest=/etc/hadoop/mapred-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
	if(a == ""):
		a=commands.getoutput("sudo ansible dn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/hdfs-site.xml dest=/etc/hadoop/hdfs-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
		if(a == ""):
			a=commands.getoutput("sudo ansible nn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/hdfsnn.xml dest=/etc/hadoop/hdfs-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
			if(a == ""):			
				a=commands.getoutput("sudo ansible sn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/hdfssn.xml dest=/etc/hadoop/hdfs-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
				if(a == ""):
					flag=0
				else:
					flag=1
			else:
				flag=1
		else:
			flag=1
	else:
		flag=1
else:
	flag=1

if(flag==1):
	print "The Ip Listed Below Are Not Reachable "+a
else:
	print "OK"

