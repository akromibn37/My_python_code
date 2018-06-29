"""
this
"""
def c_to_f(c):
	"""translate celcius to fahrenheit"""
	if c < -273.15:
		#return "Please don't write any message in the text file when input is lower than -273.15."
		return ""
	else:
		f = (c*1.8)+32
		return str(f)

temperature = [10,-20,-289,100]
file = open("exercise5.txt","w")
for temp in temperature:
	file.write(c_to_f(temp)+"\n")
	
file.close()