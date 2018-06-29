def convert(celcius):
	if celcius < -273.15:
		print("The temperature doesn't make sense")
	else:
		fahrenheit = (celcius*1.8)+32
		print(fahrenheit)

temperatures = [10,-20,-289,100]		
for temp in temperatures:
	convert(temp)
	

#money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
#print(money["under_bed"][1])