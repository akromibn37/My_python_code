print(1)
def currency_converter(rate,euros):
	dollars = euros*rate
	return dollars
r = input("Enter rate:")
e = input("Euros amount:")
d = currency_converter(int(r),float(e))
print("The dollars amount is",d)