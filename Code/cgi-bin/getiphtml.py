#!/usr/bin/python

import cgi
print "Content-type:text/html"
x=cgi.FieldStorage()
q=x.getvalue('q')
print ""
print """
	<html>
	<body>
	  <br /><br /><br />
	  <h1><center>Scanning For Live Hosts.<br />Do Not Hit Refresh</center></h1>
	</body>
	<script>
	    var xmlhttp = new XMLHttpRequest();
	    xmlhttp.open("GET", "http://192.168.43.63/cgi-bin/AJAX/getip.py", false);
       	    xmlhttp.send();
	    if (xmlhttp.responseText.trim() == 'OK')
	    {"""
if(q=='mh'):
	print """document.location="http://192.168.43.63/cgi-bin/manhadoop.py" """
else:
	print """document.location="http://192.168.43.63/cgi-bin/autohadoop.py" """
print """   }
	    else
	    {
	      alert("There was some error. Please Try Again Later");
	      document.location="http://192.168.43.63/cgi-bin/services.py"
	    }
	</script>
	
	</html>"""

