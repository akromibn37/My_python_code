import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.soccersuck.com","soccersuck.com","www.siamsport.co.th","hotmail.com","www.hotmail.com","login.live.com"]

while True:		
	if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
		print("Working hours....")
		with open(hosts_path,'r+') as file:
			content = file.read()			
			for web in website_list:
				if web in content:
					pass
				else:
					file.write("\n"+redirect+" "+web)
	else:
		with open(hosts_path,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(web in line for web in website_list):
					file.write(line)
			file.truncate()						
		print("Fun hours....")
	time.sleep(5)

