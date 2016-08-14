#!/usr/bin/python

import cgi
import commands
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

flag=1
a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/core-site.xml dest=/hadoop2/etc/hadoop/core-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
if(a == ""):
	a=commands.getoutput("sudo ansible dn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/hdfs-site.xml dest=/hadoop2/etc/hadoop/hdfs-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
	if(a == ""):
		a=commands.getoutput("sudo ansible dn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/yarn.xml dest=/hadoop2/etc/hadoop/yarn-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )	
		if(a == ""):
			a=commands.getoutput("sudo ansible nn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/hdfsnn.xml dest=/hadoop2/etc/hadoop/hdfs-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
			if(a == ""):
				a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/mapred-site.xml dest=/hadoop2/etc/hadoop/mapred-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
				if(a == ""):
					a=commands.getoutput("sudo ansible jt -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/yarnrs.xml dest=/hadoop2/etc/hadoop/yarn-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
					if(a == ""):
						a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/yarncli.xml dest=/hadoop2/etc/hadoop/yarn-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
						if(a == ""):
							a=commands.getoutput("sudo ansible sn -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/hdfssn.xml dest=/hadoop2/etc/hadoop/hdfs-site.xml' | grep 'UNREACHABLE' | awk '{print $1}' " )
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
		else:
			flag=1
	else:
		flag=1
else:
	flag=1

if(flag==0):
	print "OK"
else:
	print "The Ip Listed Below Are Not Reachable "+a
