#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/repo/hive.tar.gz dest=/root/hive.tar.gz' | grep 'UNREACHABLE' | awk '{print $1}'")
if(a == ""):
	a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'tar -zxf /root/hive.tar.gz' | grep 'UNREACHABLE' | awk '{print $1}'")
	if(a == ""):
		a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'mv /root/apache-hive-1.2.1-bin /hive' | grep 'UNREACHABLE' | awk '{print $1}'")
		if(a == ""):
			flag=0
		else:
			flag=1
	else:
		flag=1
else:
	flag=1

if(flag==0):
	print "OK"
else:
	print "The Ip is Not Reachable "+a
