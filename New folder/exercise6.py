import datetime 
import glob2

name = glob2.glob("*.txt")

def createfile():
	with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w") as file:
		for f in name:
			with open(f,'r') as fi:
				file.write(fi.read()+"\n")

createfile()