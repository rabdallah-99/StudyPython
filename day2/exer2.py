#!/usr/bin/python
#this program is for calculating students grades
name=input("Enter name : ")
finalExam = int(input("enter exam score  "))
asswssment = int(input("enter assessment score  "))
homework  = int(input("enter hw score  "))
def Grade(name,hw,exam,lab):
	result=hw+exam+lab
	perc=result/1.75
	list1=[name,perc]
	return list1
res1=Grade(name,homework,finalExam,asswssment)
print(res1)
