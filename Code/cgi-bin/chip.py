#!/usr/bin/python

import os

os.system("sed -i 's/192.168.43.145/192.168.43.63/g' /var/www/html/repo/hadoop.repo")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' index.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' reg.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' forg.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' login.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' register.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' forgot.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' /var/www/cgi-bin/AJAX/testpass.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' /var/www/cgi-bin/AJAX/testuser.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' /var/www/cgi-bin/AJAX/testuserexist.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' services.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' update.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' chngpass.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' delete.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' logout.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' getiphtml.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' /var/www/cgi-bin/AJAX/getip.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' manhadoop.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' mancluster.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' mancluster1.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' autohadoop.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' autohadoop1.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' upload.py")
os.system("sed -i 's/192.168.43.145/192.168.43.63/g' upload1.py")

