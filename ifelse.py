hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
diff = h
if h>40:
	diff = h-40
	h = 40
elif h<=40:
	diff = 0
diffrate = r*1.5
#print(r)
#print(diffrate)
#print(diff)
#print(diff*diffrate)
#print(h*r)
sum = (h*r) + (diff*diffrate)
print(sum)