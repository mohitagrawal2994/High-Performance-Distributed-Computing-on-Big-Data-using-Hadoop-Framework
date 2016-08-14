#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
x=cgi.FieldStorage()
uid=x.getvalue('uid')
h=x.getvalue('h')
p=x.getvalue('p')
print ""

flag=0
exp="# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n\t. /etc/bashrc\nfi\n"

if((h=="1")&(p=="1")):
	bash=exp.replace('/etc/bashrc\nfi\n','/etc/bashrc\nfi\n\nexport HIVE_HOME=/hive\nexport PATH=$HIVE_HOME/bin:$PATH\nexport PIG_HOME=/pig\nexport PATH=$PIG_HOME/bin:$PATH')
	f=open('/var/www/html/IP/'+uid+'/bash.txt','w')
	f.write(bash)
	f.close()
	a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/bash.txt dest=/root/.bashrc' | grep 'UNREACHABLE' | awk '{print $1}'")
	if( a == ""):
		a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'exec bash' | grep 'UNREACHABLE' | awk '{print $1}'")
		if(a == ""):
			flag=0
		else:
			flag=1
	else:
		flag=1

elif((h=="1")&(p=="0")):
	bash=exp.replace('/etc/bashrc\nfi\n','/etc/bashrc\nfi\n\nexport HIVE_HOME=/hive\nexport PATH=$HIVE_HOME/bin:$PATH')
	f=open('/var/www/html/IP/'+uid+'/bash.txt','w')
	f.write(bash)
	f.close()
	a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/bash.txt dest=/root/.bashrc' | grep 'UNREACHABLE' | awk '{print $1}'")
	if( a == ""):
		a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'exec bash' | grep 'UNREACHABLE' | awk '{print $1}'")
		if(a == ""):
			flag=0
		else:
			flag=1
	else:
		flag=1
elif((h=="0")&(p=="1")):
	bash=exp.replace('/etc/bashrc\nfi\n','/etc/bashrc\nfi\n\nexport PIG_HOME=/pig\nexport PATH=$PIG_HOME/bin:$PATH')
	f=open('/var/www/html/IP/'+uid+'/bash.txt','w')
	f.write(bash)
	f.close()
	a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/IP/"+uid+ "/bash.txt dest=/root/.bashrc' | grep 'UNREACHABLE' | awk '{print $1}'")
	if( a == ""):
		a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'exec bash' | grep 'UNREACHABLE' | awk '{print $1}'")
		if(a == ""):
			flag=0
		else:
			flag=1
	else:
		flag=1
else:
	flag=0

if(flag==0):
	print "OK"
else:
	print "The Ip is Not Reachable "+a

