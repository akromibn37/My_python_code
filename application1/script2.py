import random,string

vowels = "vowels"
consonant = "bjgmqwertyuiasdof"
letter = string.ascii_lowercase

letter_input_1=input("What letter do you want?:")
letter_input_2=input("What letter do you want?:")
letter_input_3=input("What letter do you want?:")

#print(letter_input_1,letter_input_2,letter_input_3)
def generate():
	if letter_input_1=='v':
		letter1 = random.choice(vowels)
	elif letter_input_1=='c':
		letter1 = random.choice(consonant)
	elif letter_input_1=='l':
		letter1 = random.choice(letter)
	else:
		letter1 = letter_input_1
	
	if letter_input_2=='v':
		letter2 = random.choice(vowels)
	elif letter_input_2=='c':
		letter2 = random.choice(consonant)
	elif letter_input_2=='l':
		letter2 = random.choice(letter)
	else:
		letter2 = letter_input_2
	
	if letter_input_3=='v':
		letter3 = random.choice(vowels)
	elif letter_input_3=='c':
		letter3 = random.choice(consonant)
	elif letter_input_3=='l':
		letter3 = random.choice(letter)
	else:
		letter3 = letter_input_3
	
	name = letter1+letter2+letter3
	return name

for i in range(20):
	print(generate())
	