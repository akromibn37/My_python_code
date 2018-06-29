class account:
	
	def __init__(self,filepath):
		self.filepath=filepath
		with open(filepath, 'r') as file:
			self.balance=int(file.read())
			
	def withdraw(self,amount):
		self.balance=self.balance - amount
		
	def deposit(self,amount):
		self.balance=self.balance + amount
		
	def commit(self):
		with open(self.filepath, 'w') as file:
			file.write(str(self.balance))
		
		
#acc=account("balance.txt")
#print(acc.balance)		
#acc.withdraw(100)
#print(acc.balance)
#acc.deposit(500)	
#print(acc.balance)
#acc.commit()
	
class checking(account):
	
	def __init__(self,filepath,fee):
		account.__init__(self,filepath)
		self.fee=fee
		
	def transfer(self,amount):
		self.balance=self.balance-amount-self.fee

check=checking("balance.txt",10) 
check.transfer(300)
check.commit()
print(check.balance)
