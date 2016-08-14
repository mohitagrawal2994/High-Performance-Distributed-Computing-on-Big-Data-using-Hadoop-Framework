#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m yum -a 'name=jdk state=present' | grep 'UNREACHABLE' | awk '{print $1}'")
if( a == ""):
	print "OK"
else:
	print "The Ip Listed Below Are Not Reachable "+a
