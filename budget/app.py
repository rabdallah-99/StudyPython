#!/usr/bin/python
from datetime import date
from budget import Budget
#this is budget app it has the following features
#1) create budget feature
#2) withdraw feature
#3) Deposit feature
#4) show transactions
#5) Transfer money between budgets
#6) put spend limit
print("\t\t\t \u001b[31m Budget \t\t\t\u001b[0m \n")
choice=True
list=[]
while choice :
	print ("\u001b[34m 1) Create Budget. \n")
	print(" 2) Withdraw \n")
	print(" 3) Deposit \n")
	print(" 4) Display transactions \n")
	print(" 5) Transfer between budgets \n")
	print(" 6) Set spend limit \n")
	print(" 7) Display budget info \n")
	print(" 8) Exit \n")
	x=input("enter your choice : ")
	if x == "8" :
		choice = False
	elif x == "1" :
		print ("\u001b[33m")
		category=input("please enter budget name: ")
		balance=int(input("please enter the starting balance for the budget: "))
		limit=int(input("please enter the limit: "))
		budget=Budget(balance,limit,category)
		list.append(budget)
	elif x == "2" :
		print ("\u001b[33m")
		category=input("please enter the budget name: ")
		amount=int(input("please enter the amount to withdraw: "))
		flag = True
		for budget in list :
			if budget.category == category :
				flag = False
				if budget.balance >= amount :
					budget.withdraw(amount)
				else :
					print("Not enough money left")
				break
		if flag :
				print("budget not found")
			
	elif x == "3" :
		print ("\u001b[33m")
		category=input("please enter the budget name: ")
		amount=int(input("please enter the amount to deposit: "))
		flag=True
		for budget in list :
			if budget.category == category :
				flag=False
				if (budget.balance+ amount) < budget.limit :
					budget.deposit(amount)
				else :
					print("Limit exceeded transaction dropped")
				break
		if flag :
				print("budget not found")

	elif x == "4" :
		print ("\u001b[33m")
		category=input("please enter the budget name: ")
		flag = True
		for budget in list :
			if budget.category == category :
				flag = False
				budget.display()
		if flag :
				print("budget not found")
	elif x == "5" :
		print ("Transfer")
	elif x == "6" :
		print ("\u001b[33m")
		category=input("please enter the budget name: ")
		limit=int(input("please enter the new limit: "))
		flag = True
		for budget in list :
			if budget.category == category :
				flag = False
				budget.limit=limit
		if flag :
				print("budget not found")
	elif x == "7" :
		print ("\u001b[33m")
		category=input("please enter the budget name: ")
		flag = True
		for budget in list :
			if budget.category == category :
				flag = False
				print(budget)
		if flag :
				print("budget not found")
	else :
		print("please enter a valid choice \u001b[0m")
