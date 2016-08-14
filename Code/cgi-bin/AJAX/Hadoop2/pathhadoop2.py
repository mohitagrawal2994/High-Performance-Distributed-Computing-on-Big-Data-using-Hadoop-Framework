#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

a="# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n\t. /etc/bashrc\nfi\n\nexport JAVA_HOME=/usr/java/jdk1.7.0_79\nexport PATH=$JAVA_HOME/bin:$PATH\nexport HADOOP_HOME=/hadoop2\nexport PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH\n"

f=open('/var/www/html/IP/'+uid+'/bash.txt','w')
f.write(a)
f.close()

a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/bash.txt dest=/root/.bashrc' | grep 'UNREACHABLE' | awk '{print $1}'")

if( a ==""):
	a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'exec bash' | grep 'UNREACHABLE' | awk '{print $1}'")
	if( a == ""):
		print "OK"
	else:
		print "The Ip Listed Below Are Not Reachable "+a
else:
	print "The Ip Listed Below Are Not Reachable "+a
