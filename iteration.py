largest = 0
smallest = None
while True:
	num = input("Enter a number: ")
	if num == "done" :
	    break
	try:
	    fval = float(num)		
	except:
	    print('Invalid input')
	    continue    
	if fval>largest:
	    largest = fval
	if smallest is None:
	    smallest = fval
	elif fval<smallest:
	    smallest = fval		
print("Maximum is", int(largest)) 
print("Minimum is", int(smallest)) 