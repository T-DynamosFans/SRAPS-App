import settings_conf
import os
logs = settings_conf.logs
update = settings_conf.update
accent = settings_conf.accent
primary = settings_conf.primary
getSettings =  lambda : {"logs":logs,"update":update,"accent":accent,"primary":primary}

def writeSettings(set,data):
		if "logs" in set:
			data1 = f"""
logs = {data}	
update = {update}
accent = "{accent}"
primary = "{primary}"		
	"""
		elif "update" in set:
			data1 = f"""
logs = {logs}	
update = {data}
accent = "{accent}"
primary = "{primary}"		
	"""			
		elif "accent" in set:
			data1 = f"""
logs = {logs}	
update = {update}
accent = "{data}"
primary = "{primary}"	
	"""
		elif "primary" in set:
			data1 = f"""
logs = {logs}	
update = {update}
accent = "{accent}"
primary = "{data}"		
	"""					
		file2 = open('settings_conf.py', 'w')
		print(data)
		file2.write(data1)
		