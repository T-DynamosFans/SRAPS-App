logs = True
update = True

getSettings =  lambda : {"logs":logs,"update":update}

def writeSettings(set,data):
	with open(r'settings.py', 'rw') as file:
		data = file.read()
		if f"{set} = True" in data:
			data = data.replace(f"{set} = True", f"{set} = {data}")
		elif f"{set} = False" in data:
			data = data.replace(f"{set} = False", f"{set} = {data}") 
		file.write(data)
		