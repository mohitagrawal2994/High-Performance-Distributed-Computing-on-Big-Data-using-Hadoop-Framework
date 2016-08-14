#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
print ""

flag=1

a=commands.getoutput("sudo ansible nn -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop namenode -format' | grep 'UNREACHABLE' | awk '{print $1}'")
if(a==""):
	a=commands.getoutput("sudo ansible nn -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop-daemon.sh start namenode' | grep 'UNREACHABLE' | awk '{print $1}'")
	if(a==""):
		a=commands.getoutput("sudo ansible jt -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop-daemon.sh start jobtracker' | grep 'UNREACHABLE' | awk '{print $1}'")	
		if(a==""):
			a=commands.getoutput("sudo ansible dn -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop-daemon.sh start datanode' | grep 'UNREACHABLE' | awk '{print $1}'")
			if(a==""):
				a=commands.getoutput("sudo ansible dn -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop-daemon.sh start tasktracker' | grep 'UNREACHABLE' | awk '{print $1}'")
				if(a==""):
					a=commands.getoutput("sudo ansible sn -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop-daemon.sh start secondarynamenode' | grep 'UNREACHABLE' | awk '{print $1}'")
					if(a==""):
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

if(flag==0):
	print "OK"
else:
	print "The Ip Listed Below Are Not Reachable "+a

