#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/repo/rhel7rpm/hadoop-1.2.1-1.x86_64.rpm dest=/root/hadoop.rpm' | grep 'UNREACHABLE' | awk '{print $1}'")
if( a == ""):
	print "OK"
else:
	print "The Ip Listed Below Are Not Reachable "+a
