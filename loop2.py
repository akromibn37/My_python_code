names = ["a","b","c"]
emaildomain = ["gmail","hotmail","yahoo"]

for i,j in zip(names,emaildomain):
	text = i+"@"+j
	print(text)