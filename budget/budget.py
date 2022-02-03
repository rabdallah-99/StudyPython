#!/usr/bin/python
from datetime import date
class Budget :
	def __init__(self,balance,limit,category) :
		self.balance=balance
		self.limit=limit
		self.category=category
		self.transaction(balance,"Create")
	def withdraw(self,amount):
		self.balance -= amount
		self.transaction(amount,"withdraw")
		return amount
	def transaction(self,amount,operation):
		today=date.today()
		file=open(self.category,"a")
		transaction=f"{today}:{operation}:{amount}:{self.balance}"
		file.write(transaction)
		file.write("\n")
		file.close
		
	def deposit(self,amount):
		self.balance += amount
		self.transaction(amount,"deposit")
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
