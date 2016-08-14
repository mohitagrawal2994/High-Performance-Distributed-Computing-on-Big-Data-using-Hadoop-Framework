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

	print """
		<head>
		<script>"""
	if(q=='insuffip'):
		print "alert('There Are Not Sufficient IPs To Make The Cluster');"
	
	print """ var xAngle=0, yAngle=0;
	    	  function whichButton(event) 
	          {
	            switch(event.keyCode) 
              	    {
                      case 37:
                      yAngle -=90;
                      break;
      
       		      case 38:
      		      xAngle +=90;
      		      break;
   
      		      case 39:
       		      yAngle +=90;
      		      break;

      		      case 40:
                      xAngle -=90;
     		      break;
    	            };
                    document.getElementById("cube1").style.transform = "rotateX("+xAngle+"deg) rotateY("+yAngle+"deg)";
                  }
  
		</script>
		<link rel="stylesheet" type="text/css" href="http://192.168.43.63/css/base.css">
		<style>
		  #cube													/* Styling For Cube */
   		  {
      		    position:absolute;
      		    top:40%;
                    left:45%;
                    perspective:280px;
                    perspective-origin:50% 50%;
                  }
    		  #cube1
                  {
      		    position:relative;
      		    margin:auto;
      		    height:180px;
                    width:180px;
		    transition: transform 2s linear;
                    transform-style:preserve-3d;
	    	  }
		  .face 
    		  {
	            position:absolute;
	            height:130px;
	            width:130px;
	            padding:20px;
	            background-color:rgba(0, 0, 0, 0.9);
	            border:2px solid red;
                  }
    		  #f1
	    	  {
	      	    transform: rotateX(90deg) translateZ(90px);
	    	  }
	    	  #f2
	    	  {
	      	    transform: translateZ(90px);
	    	  }
	    	  #f3
	    	  {
	      	    transform: rotateY(90deg) translateZ(90px);
	    	  }
	    	  #f4
	    	  {
	      	    transform: rotateY(180deg) translateZ(90px);
	    	  }
	    	  #f5
	    	  {
	      	    transform: rotateY(-90deg) translateZ(90px);
	    	  }
	    	  #f6
	    	  {
	      	    transform: rotateX(-90deg) translateZ(90px) rotate(180deg);
	    	  }
 
		</style>
		<body onkeyup="whichButton(event)" style="background: url('http://192.168.43.63/backgrounds/Body2.jpg') no-repeat top right;">
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
			<div id="cube" name="cube">
			  <div id="cube1" name="cube1">
			    <div class="face" id="f1">
			    </div>
			    <div class="face" id="f2">
	   		      <center style="font-size:20px;color:white;position:absolute;top:20%;left:11%;">Press &uarr;,&darr;,&rarr; & &larr;<br /> To<br /> Rotate<br /> &<br /> Click To Select</center>
			    </div>
			    <div class="face" id="f3">
			      <a href="http://192.168.43.63/cgi-bin/getiphtml.py?q=mh"><center style="font-size:20px;color:white;position:absolute;top:30%;left:32%;">Manual<br /> Hadoop<br /> Setup</center></a>
			    </div>
			    <div class="face" id="f4">
			      <a href="http://192.168.43.63/cgi-bin/upload.py"><center style="font-size:20px;color:white;position:absolute;top:20%;left:35%;">Upload<br />Files<br />To<br />Cluster</center></a>
			    </div>
			    <div class="face" id="f5">
			      <a href="http://192.168.43.63/cgi-bin/getiphtml.py?q=ah"><center style="font-size:20px;color:white;position:absolute;top:30%;left:28%;">Automatic<br /> Hadoop<br /> Setup</center></a>
			    </div>
			    <div class="face" id="f6">
			      f6
			    </div>
			  </div>
			</div>
			
			
		</body>
		</html>"""
	
