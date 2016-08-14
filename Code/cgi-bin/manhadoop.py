#!/usr/bin/python

import cgi
import commands
import os
import Cookie
import datetime
import MySQLdb as mariadb
print "Content-type:text/html"
x=cgi.FieldStorage()
q=x.getvalue('q')
w=x.getvalue('w')
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
				cursor.execute("select FULLNAME from USERS where USERNAME=%s",(a[0]))
				mariadb_connection.commit()
				for FULLNAME in cursor:
					a=FULLNAME
					name=a[0]
					flag=0
					mariadb_connection.close()					
					break;
					

		else:
			flag=1

except:
	flag=1

if(flag==1):
	print "location:http://192.168.43.63/cgi-bin/index.py?q=merror"
	print ""
	
else:	
	print ""
	if(q=='ferror'):
		print "<script>alert('There Was Error In The Data You Submitted');</script>"
	if(q=='merror'):
		print "<script>alert('There Was Error In The Database.');</script>"
	if(q=='iperror'):
		print "<script>alert('Please Select IPs of Live Hosts');</script>"
	if(q=='ipuerror'):
		print "<script>alert('The Ip Listed Below Are Not Reachable "+w+ ". Plz check for network connection or restart SSH services');</script>"
	print """<link rel="stylesheet" type="text/css" href="http://192.168.43.63/css/base.css">
		 <style>
		   #ip
		   {
			position:absolute;
			top:30%;
			left:15%;
			height:50%;
			width:15%;
			padding:20px;
			font-size:18px;
			background-color:yellow;
		   }
		   #ip1
		   {
			padding-left:20%;
		   }
		   #fm
		   {
			position:absolute;
			top:30%;
			right:10%;
			font-size:15px;
		   }
		 </style>
		 <body style="background: url('http://192.168.43.63/backgrounds/Body3.jpg') no-repeat top right;">
		   <div id="top" name="top">
			  <div id="top1" name="top1">
			    Ha2uP<br /><span style="position:relative;left:15%;">SoLuTiOns</span>
			  </div>
			  <div id="top2" name="top2">
			    <a href="http://192.168.43.63/cgi-bin/services.py"><b>SERVICES</b></a>
			  </div>
			</div>
			<div id="bar" name="bar">"""
	print "<span id='images' name='images' style='position:absolute;top:11%;left:10%;'><img src='http://192.168.43.63/pic/"+uid+ "' height='35' width='35' ></img></span></div>"
	print "<div id='userid' name='userid'><i>Welcome "+name+ " </i></div>" 
	print """	<div id="list" name="list">
			  <ul id="list1" name="list1">
			    <li style="font-size:20px;"><img src="http://192.168.43.63/backgrounds/set.png" />Settings
			      <ul style="margin-top:8%;">
				<li><a href="http://192.168.43.63/cgi-bin/update.py">Update Details</a></li>
				<li><a href="http://192.168.43.63/cgi-bin/chngpass.py">Change Password</a></li>
				<li><a href="http://192.168.43.63/cgi-bin/delete.py">Delete My Account</a></li>
				<li><a href="http://192.168.43.63/cgi-bin/logout.py">Logout</a></li>
			      </ul></li>
			  </ul>
			</div>
			<div id="ip" name="ip">
			  <u style="margin-left:20%;">LIVE HOSTS</u><br /><br /><div id="ip1" name="ip1"> """	
	f1=open('/var/www/html/IP/'+uid+ '/IPR.txt','r')
	a=f1.read()
	b=a.split("\n")
	c=len(b)
	for i in range(0,c):
		print b[i]
		print "<br />"
	  		
	print """       </div>  
			</div>
			<div id="fm" name="fm">
			  <form method="post" action="http://192.168.43.63/cgi-bin/mancluster.py" autocomplete="off">
				<fieldset style="border:double;border-radius:0px 40px 0px 40px;"><legend><i>Cluster Settings</i></legend>
					<pre>					
Client IP             :   <input type="text" id="cli" name="cli" autofocus="required" required><br />	
Namenode IP           :   <input type="text" id="nn" name="nn" required><br />
Secondary Namenode IP :   <input type="text" id="sn" name="sn" required><br />
Backup Namenode IP    :   <input type="text" id="bn" name="bn" required><br />	
Job Tracker IP        :   <input type="text" id="jt" name="jt" required><br />	
Datanode Range        :   <input type="text" id="dn1" name="dn1" required><b>-</b><input type="text" id="dn2" name="dn2" required><br />
Hadoop Version        :   <input type="radio" id="hd" name="hd" value="1" required />Hadoop 1.2.1      <input type="radio" id="hd" name="hd" value="2" required />Hadoop 2.6.4<br />
Frameworks            :   <input type="checkbox" id="hive" name="hive" value="1" />HIVE  <input type="checkbox" id="pig" name="pig" value="1" />PIG  <input type="checkbox" id="splunk" name="splunk" value="1" />SPLUNK<br /><br />
		<input type="submit" style="border-radius:30px 30px 30px 30px;"/>			<input type="reset" style="border-radius:30px 30px 30px 30px;"/>
			  </pre></fieldset></form>
			</div>
		   </body>
		 </html>"""

