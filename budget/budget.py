#!/usr/bin/python
from datetime import date
class Budget :
	def __init__(self,balance,limit,category) :
		self.balance=balance
		self.limit=limit
		self.category=category
		file=open(category,"w")
		today=date.today()
		transaction=f"{today}:Create:{balance}:{balance}"
		file.write(transaction)
		file.write("\n")
		file.close
	def withdraw(self,amount):
		self.balance -= amount
		today=date.today()
		file=open(self.category,"a")
		transaction=f"{today}:withdraw:{amount}:{self.balance}"
		file.write(transaction)
		file.write("\n")
		file.close
		return amount
	def deposit(self,amount):
		self.balance += amount
		today=date.today()
		file=open(self.category,"a")
		transaction=f"{today}:deposit:{amount}:{self.balance}"
		file.write(transaction)
		file.write("\n")
		file.close
		return amount
	def __repr__(self):
		return f" Budget : {self.category} with balance {self.balance} and limit {self.limit}"
	def transfer(self,budget,amount):
		budget.withdraw(amount)
		self.deposit(amount)
	def display(self):
		file=open(self.category,"r")
		var=file.readlines()
		for line in var :
			print(line)
