#def make_account():
#	return{'balance': 0}

#def deposit(account, amount):
#	account['balance'] +=amount
#	return account['balance']

#def withdraw(account, amount):
#	account['balance']-=amount
#	return account['balance']

class Bank:
	def __init__(self):
		self.balance=0

	def withdraw(self,amount):
		self.balance-=amount
		return self.balance
	def deposit(self,amount):
		self.balance+=amount
		return self.balance

class MinimumBalance(Bank):
	def init(self,min_bal):
		Bank.__init__(self)
		self.min_bal=min_bal
	
	def withdraw(self,amount):
		if self.balance-amount<self.min_balance:
			print 'Sorry, minimum balance must bemaintained'
		else:
			Bank.withdraw(self,amount)

