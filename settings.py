import settings_conf
import os
logs = settings_conf.logs
update = settings_conf.update
getSettings =  lambda : {"logs":logs,"update":update}

def writeSettings(set,data):
		if "logs" in set:
			data = f"""
logs = {data}	
update = {update}		
	"""
		else:
			data = f"""
logs = {logs}	
update = {data}		
	"""			
		file2 = open('settings_conf.py', 'w')
		print(data)
		file2.write(data)
		