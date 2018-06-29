def minutes_to_hour(minutes):
	hour = minutes/60
	return hour
def second_to_hour(seconds):
	hour = seconds/3600
	return hour
def minutes(minutes,second = 360):
	hours = minutes/60 + second/3600
	return hours

print(minutes(60))
m = input("How much minutes:")
m = float(m)
h = minutes_to_hour(m)
print("hour is",h)
print(minutes_to_hour(70))
print(type(minutes_to_hour(60)))
print(second_to_hour(7200))