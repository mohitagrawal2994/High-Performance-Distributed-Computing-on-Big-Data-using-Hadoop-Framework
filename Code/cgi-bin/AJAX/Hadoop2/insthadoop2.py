#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

"""
a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'tar -zxf /root/hadoop2.tar.gz' | grep 'UNREACHABLE' | awk '{print $1}'")
if( a == ""):
	a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'mv /root/hadoop-2.6.4 /hadoop2' | grep 'UNREACHABLE' | awk '{print $1}'")
	if(a == ""):
		print "OK"
	else:
		print "The Ip Listed Below Are Not Reachable "+a	
else:
	print "The Ip Listed Below Are Not Reachable "+a

"""

print "OK"

