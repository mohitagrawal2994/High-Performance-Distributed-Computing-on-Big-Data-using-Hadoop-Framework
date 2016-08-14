#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

"""
a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/repo/hadoop2.tar.gz dest=/root/hadoop2.tar.gz' | grep 'UNREACHABLE' | awk '{print $1}'")
if( a == ""):
	print "OK"
else:
	print "The Ip Listed Below Are Not Reachable "+a

"""

print "OK"

