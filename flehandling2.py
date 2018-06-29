import datetime

now = datetime.datetime.now()
filename = "sample.txt"

def createfile():
	with open(str(now.strftime("%Y-%m-%d-%H-%M")+".txt"),"w") as file:
		file.write("")

createfile()
