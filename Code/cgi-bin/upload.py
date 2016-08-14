#!/usr/bin/python

import os
import cgi
import Cookie
import datetime
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
q=x.getvalue('q')
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
					mariadb_connection.close()
					flag=0
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
		print "<script>alert('Select A File To Upload To Cluster');</script>"
	print """<link rel="stylesheet" type="text/css" href="http://192.168.43.63/css/base.css">
		 <style>
		   #fm
		   {
			position:absolute;
			top:40%;
			left:25%;
			font-size:15px;
		   }
		 </style>
		 <script>
		   function ajax()
		   {
			var xmlhttp = new XMLHttpRequest();"""
	print "         xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/clusterexist.py?uid="+uid+ "', false);"
	print "		xmlhttp.send();"
	print """	if(xmlhttp.responseText.trim() != 'OK')
		 	{
			  alert('Please Create A Cluster First To Upload Files');
			  document.location="http://192.168.43.63/cgi-bin/services.py"
	         	}
		   }
		 </script>
		 </head>
		 <body style="background: url('http://192.168.43.63/backgrounds/Body3.jpg') no-repeat top right;" onload=ajax()>
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
		 <div id="fm" name="fm">
		   <form method="post" action="http://192.168.43.63/cgi-bin/upload1.py" enctype="multipart/form-data" autocomplete="off">
		     <fieldset style="border:double;border-radius:0px 40px 0px 40px;"><legend><i>Upload Files</i></legend>
		       <pre>		
File To Be Uploaded : <input type="file" id="fu" name="fu" required /><br /><br />
		     <input type="submit" />
		   </pre></fieldset></form>
	         </div>
		 </body>
		</html>
		"""
