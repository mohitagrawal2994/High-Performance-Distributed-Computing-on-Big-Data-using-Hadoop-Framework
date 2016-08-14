#!/usr/bin/python

import cgi
import commands
import os
import Cookie
import datetime
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
w=x.getvalue('w')
h=x.getvalue('h')
p=x.getvalue('p')
s=x.getvalue('s')

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
			cursor.execute("update COOKIE set AUTOLOGOUT=%s where CNO=%s",(future,b))
			mariadb_connection.commit()
			cursor.execute("select USERNAME from COOKIE where CNO=%s",(b))
			mariadb_connection.commit()
			for USERNAME in cursor:
				a=USERNAME
				uid=a[0]
				flag=0
				break;

except:
	flag=1

if(flag==1):
	print "location:http://192.168.43.63/cgi-bin/manhadoop.py?q=merror"
	print ""
else:
	print ""
	print """
		<html>
		<head>
	     	  <style>
		    #mybar
		    {
		      position:absolute;
		      top:40%;
		      left:15%;
		      height:5%;
		      width:1%;
		      background-color:green;
		    }
		    #tex
		    {
		      position:absolute;
		      top:43%;
		      left:45%;
		    }
		  </style>
		</head>
		<body>
		  <br /><br /><br />
		  <h1><center id="page" name="page">Your Cluster Is Being Set Up<br />Do Not Hit Refresh</center></h1>
		  <div id="pbar" name="pbar">
		    <div id="mybar">
		      <center id="progress" name="progress">0%</center>
		    </div>
		    <p id="tex" name="tex">Installing JDK</p>
		  </div>
		  </body>
		  <script>
		    var width=1;
		    var flag=1;
		    var xmlhttp = new XMLHttpRequest();"""
	if(w=='1'):
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/jdk.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		   	   width=width*100;
		   	   document.getElementById('mybar').style.width=width;
		   	   document.getElementById('progress').innerHTML="10%";
		   	   document.getElementById('tex').innerHTML="Copying Hadoop";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/hadoop1.py?uid="+uid+ "', false);"
       		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*300;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="30%";
		           document.getElementById('tex').innerHTML="Installing Hadoop";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/insthadoop1.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*500;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="50%";
		           document.getElementById('tex').innerHTML="Generating Configuration Files";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/confighadoop1.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*600;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="60%";
		           document.getElementById('tex').innerHTML="Copying The Configuration Files";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/concopyhadoop1.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*750;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="75%";
		           document.getElementById('tex').innerHTML="Starting Hadoop Services";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/starthadoop1.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*900;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="90%";	
			   document.getElementById('tex').innerHTML="Installing Frameworks";
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
		 	 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 """
	else:
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/jdk.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
			   width=1
		   	   width=width*100;
		   	   document.getElementById('mybar').style.width=width;
		   	   document.getElementById('progress').innerHTML="10%";
		   	   document.getElementById('tex').innerHTML="Copying Hadoop";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/hadoop2.py?uid="+uid+ "', false);"
       		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*200;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="20%";
		           document.getElementById('tex').innerHTML="Installing Hadoop";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/insthadoop2.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*300;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="30%";
		           document.getElementById('tex').innerHTML="Setting Hadoop Paths";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/pathhadoop2.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*500;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="50%";
		           document.getElementById('tex').innerHTML="Generating Configuration Files";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/confighadoop2.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*600;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="60%";
		           document.getElementById('tex').innerHTML="Copying The Configuration Files";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/concopyhadoop2.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*700;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="70%";
		           document.getElementById('tex').innerHTML="Starting Hadoop Services";"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/starthadoop2.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {"""
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/starthadoop21.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
		           width=1;
		           width=width*900;
		           document.getElementById('mybar').style.width=width;
		           document.getElementById('progress').innerHTML="90%";
		           document.getElementById('tex').innerHTML="Installing Frameworks";
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
		 	 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
		    	 }
		         else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }"""
	
	if(w=='1'):
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/bash1.py?uid="+uid+ "&h="+h+ "&p="+p+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }"""	
	else:
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/bash2.py?uid="+uid+ "&h="+h+ "&p="+p+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }"""	
	
	if(h == '1'):
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/hive.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }"""	
	if(p == '1'):
		if(w == '1'):
			print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop1/pigmapred1.py?uid="+uid+ "', false);"
			print "xmlhttp.send();"
			print """if(xmlhttp.responseText.trim() == 'OK')
				 {"""
			print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/pig.py?uid="+uid+ "', false);"
			print "xmlhttp.send();"
			print """if(xmlhttp.responseText.trim() == 'OK')
		         	{
			 	}
				 else
				 {
				   alert(xmlhttp.responseText);
				   document.location="http://192.168.43.63/cgi-bin/services.py"
				 }
				 }
				 else
				 {
				   alert(xmlhttp.responseText);
				   document.location="http://192.168.43.63/cgi-bin/services.py"
				 }
				 """			
		else:
			print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/Hadoop2/pigmapred2.py?uid="+uid+ "', false);"
			print "xmlhttp.send();"
			print """if(xmlhttp.responseText.trim() == 'OK')
				 {"""
			print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/pig.py?uid="+uid+ "', false);"
			print "xmlhttp.send();"
			print """if(xmlhttp.responseText.trim() == 'OK')
		         	{
			 	}
				 else
				 {
				   alert(xmlhttp.responseText);
				   document.location="http://192.168.43.63/cgi-bin/services.py"
				 }
				 }
				 else
				 {
				   alert(xmlhttp.responseText);
				   document.location="http://192.168.43.63/cgi-bin/services.py"
				 }
				 """			
	if(s == '1'):
		print "xmlhttp.open('GET', 'http://192.168.43.63/cgi-bin/AJAX/splunk.py?uid="+uid+ "', false);"
		print "xmlhttp.send();"	
		print """if(xmlhttp.responseText.trim() == 'OK')
		         {
			 }
			 else
			 {
			   alert(xmlhttp.responseText);
			   document.location="http://192.168.43.63/cgi-bin/services.py"
			 }"""	
	print """document.getElementById('tex').innerHTML="Your Cluster Has Been Setup";"""
	print "alert('Your Cluster Has Been Setup');"	
	print """document.location="http://192.168.43.63/cgi-bin/services.py"
		</script>
		</html>"""

