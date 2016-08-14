#!/usr/bin/python

print "Content-type:text/html"
print ""

print """
	<html>
	<head>
	</head>
	<body>
		<h1>this is b</h1>
		<script>
			var xmlhttp = new XMLHttpRequest();
	  		 xmlhttp.open("GET", "http://192.168.43.145/cgi-bin/test/a.py", false);
           		xmlhttp.send();
	   		alert("hello test");
	  		 alert(xmlhttp.responseText.trim())
	   		if(xmlhttp.responseText.trim() == 'hello')
	   		{
				alert('yes');
	   		}	
		</script>
	</body>
	</html>"""
