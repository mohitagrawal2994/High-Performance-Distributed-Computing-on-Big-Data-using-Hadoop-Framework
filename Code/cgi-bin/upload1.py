#!/usr/bin/python

import os
import cgi
import Cookie
import datetime
import commands
import MySQLdb as mariadb

print "Content-type:text/html"
x=cgi.FieldStorage()
fileitem=x['fu']

if fileitem.filename:
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
		fn = os.path.basename(fileitem.filename)
        	open('../html/file/'+uid+ '/'+fn, 'wb').write(fileitem.file.read())
		a=commands.getoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m copy -a 'src=/var/www/html/file/"+uid+ "/"+fn+ " dest=/root/"+fn+ "' | grep 'UNREACHABLE' | awk '{print $1}'")
		if(a == ""):
			a=commands.getstatusoutput("sudo ansible cli -i /var/www/html/IP/"+uid+ "/ans.txt -m command -a 'hadoop fs -put /root/"+fn+ " /' ")
			if(a[0] == 0):
				flag=0
			else:
				flag=1
		else:
			flag=1
		
		if(flag==0):
			print ""
			print "<script>alert('The file "+fn+ " was uploaded successfully');</script>"
			print """<script>document.location="http://192.168.43.63/cgi-bin/services.py"</script>"""
		else:
			if(a[0] == 512):
				print ""
				print "<script>alert('A file with same name "+fn+ " is already in the cluster');</script>"
				print """<script>document.location="http://192.168.43.63/cgi-bin/services.py"</script>"""
			else:
				print ""
				print "<script>alert('Cluster is unreachable at the moment');</script>"
				print """<script>document.location="http://192.168.43.63/cgi-bin/services.py"</script>"""
		os.system("rm -rf /var/www/html/file/"+uid+ "/"+fn)

else:
	print "location:http://192.168.43.63/cgi-bin/upload.py?q=ferror"
	print ""
