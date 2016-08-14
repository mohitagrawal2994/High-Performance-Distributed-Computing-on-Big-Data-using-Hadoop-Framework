#!/usr/bin/python

import cgi
import os
import Cookie
import datetime
import commands
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
cli=x.getvalue('cli')
nn=x.getvalue('nn')
sn=x.getvalue('sn')
bn=x.getvalue('bn')
jt=x.getvalue('jt')
dn1=x.getvalue('dn1')
dn2=x.getvalue('dn2')
hd=x.getvalue('hd')
h=x.getvalue('hive')
p=x.getvalue('pig')
s=x.getvalue('splunk')

if h:
	hive="Y"
else:
	h="0"
	hive="N"
if p:
	pig="Y"
else:
	p="0"
	pig="N"
if s:
	splunk="Y"
else:
	s="0"
	splunk="N"

cli=cgi.escape(cli)
nn=cgi.escape(nn)
sn=cgi.escape(sn)
bn=cgi.escape(bn)
jt=cgi.escape(jt)
dn1=cgi.escape(dn1)
dn2=cgi.escape(dn2)
hd=cgi.escape(hd)
h=cgi.escape(h)
p=cgi.escape(p)
s=cgi.escape(s)

dn1in=int(dn1[11:])
dn2in=int(dn2[11:])

flag=0

if((cli == "")| (nn == "")| (sn == "")| (bn == "")| (jt == "")| (dn1 == "")| (dn2 == "")| (hd == "")):
	flag=1
elif((cli==nn)| (cli==sn)| (cli==bn)| (cli==jt)| (nn==sn)| (nn==bn)| (nn==jt)| (sn==bn)| (sn==jt)| (bn==jt)):
	flag=1
else:
	for i in range(dn1in,dn2in+1):
		if((int(cli[11:]) == i)| (int(nn[11:])==i)| (int(sn[11:])==i)| (int(bn[11:])==i)| (int(jt[11:])==i)):
			flag=1	

if(flag==1):
	print "location:http://192.168.43.63/cgi-bin/manhadoop.py?q=ferror"
	print ""
else:
	a=[]
	flag=1
	f=datetime.datetime.now().replace(microsecond=0)
	future=datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=1)
	try:
		cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		b=cookie["Ha2uPSoLuTiOns"].value
		mariadb_connection=mariadb.connect(user='hadoop')
		cursor=mariadb_connection.cursor()
		cursor.execute("use hs")
		cursor.execute("select AUTOLOGOUT from COOKIE")
		mariadb_connection.commit()
		for AUTOLOGOUT in cursor:
			a=AUTOLOGOUT
			if(a[0] < f):
				cursor.execute("delete from COOKIE where AUTOLOGOUT=%s",(a[0]))
				mariadb_connection.commit()
			
		cursor.execute("select CNO from COOKIE")
		mariadb_connection.commit()
		for CNO in cursor:
			a=CNO
			if(a[0] == b):
				cursor.execute("update COOKIE set AUTOLOGOUT=%s where CNO=%s",(future,a[0]))
				mariadb_connection.commit()
				cursor.execute("select USERNAME from COOKIE where CNO=%s",(a[0]))
				mariadb_connection.commit()
				for USERNAME in cursor:
					a=USERNAME
					uid=a[0]
					flag=0
				cursor.execute("select PASSWORD from COOKIE where CNO=%s",(b))
				mariadb_connection.commit()
				for PASSWORD in cursor:
					a=PASSWORD
					pass1=a[0]
					flag=0					
			else:
				flag=1

	except:
		flag=1

	if(flag==1):
		print "location:http://192.168.43.63/cgi-bin/index.py?q=merror"
		print ""
	else:
		f1=open('/var/www/html/IP/'+uid+ '/ans.txt','w')
		a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+cli+ " | awk '{print $1}'")
		if(a == ""):
			flag=1
		else:
			f1.write("[cli]\n")
			f1.write(a)
			f1.write("\t")
			f1.write("ansible_ssh_user=root\t")
			f1.write("ansible_ssh_pass="+pass1+ " \n")
		a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+nn+ " | awk '{print $1}'")
		if(a == ""):
			flag=1
		else:
			f1.write("[nn]\n")
			f1.write(a)
			f1.write("\t")
			f1.write("ansible_ssh_user=root\t")
			f1.write("ansible_ssh_pass="+pass1+ " \n")
		a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+sn+ " | awk '{print $1}'")
		if(a == ""):
			flag=1
		else:
			f1.write("[sn]\n")
			f1.write(a)
			f1.write("\t")
			f1.write("ansible_ssh_user=root\t")
			f1.write("ansible_ssh_pass="+pass1+ " \n")
		a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+bn+ " | awk '{print $1}'")
		if(a == ""):
			flag=1
		else:
			f1.write("[bn]\n")
			f1.write(a)
			f1.write("\t")
			f1.write("ansible_ssh_user=root\t")
			f1.write("ansible_ssh_pass="+pass1+ " \n")
		a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+jt+ " | awk '{print $1}'")
		if(a == ""):
			flag=1
		else:
			f1.write("[jt]\n")
			f1.write(a)
			f1.write("\t")
			f1.write("ansible_ssh_user=root\t")
			f1.write("ansible_ssh_pass="+pass1+ " \n")

		f1.write("[dn]\n")
		for i in range(dn1in,dn2in+1):
			ip=str(i)
			ip1="192.168.43."+ip
			a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+ip1+ " | awk '{print $1}'")
			if(a==""):
				pass;
			else:
				f1.write(ip1)
				f1.write("\t")
				f1.write("ansible_ssh_user=root\t")
				f1.write("ansible_ssh_pass="+pass1+ " \n")
				
		f1.close()
		
		if(flag==1):
			print "location:http://192.168.43.63/cgi-bin/manhadoop.py?q=iperror"
			print ""
		else:
			cursor.execute("insert into CLUSTER(USERNAME,HADOOPV,HIVE,PIG,SPLUNK,CLIENT,NAMENODE,SNAMENODE,BNAMENODE,JOBTRACKER) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(uid,hd,hive,pig,splunk,cli,nn,sn,bn,jt));
			mariadb_connection.commit()
			for i in range(dn1in,dn2in+1):
				ip=str(i)
				ip1="192.168.43."+ip
				a=commands.getoutput("cat /var/www/html/IP/"+uid+ "/IPR.txt | grep "+ip1+ " | awk '{print $1}'")
				if(a==""):
					pass;
				else:
					cursor.execute("insert into "+uid+ "(DATANODE) values(%s)",(ip1))
					mariadb_connection.commit()
				
			a=commands.getoutput("sudo ansible all -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/repo/hadoop.repo dest=/etc/yum.repos.d/hadoop.repo' | grep 'UNREACHABLE' | awk '{print $1}'")
			if( a == "" ):
				if(hd == "1"):
					print "location:http://192.168.43.63/cgi-bin/mancluster1.py?w=1&h="+h+ "&p="+p+ "&s="+s
					print ""
				else:
					print "location:http://192.168.43.63/cgi-bin/mancluster1.py?w=2&h="+h+ "&p="+p+ "&s="+s
					print ""
			else:
				print "location:http://192.168.43.63/cgi-bin/manhadoop.py?q=ipuerror&w="+a
				print ""



