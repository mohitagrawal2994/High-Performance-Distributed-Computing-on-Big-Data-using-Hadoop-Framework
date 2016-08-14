#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/repo/splunk.rpm dest=/root/splunk.rpm' | grep 'UNREACHABLE' | awk '{print $1}'")
if(a == ""):
	a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'rpm -ivh /root/splunk.rpm --replacefiles' | grep 'UNREACHABLE' | awk '{print $1}'")
	if(a == ""):
		flag=0
	else:
		flag=1
else:
	flag=1

if(flag == 0):
	print "OK"
else:
	print "The Ip is Not Reachable "+a
