import os
os.system('clear')
#they have names and a parentheses and can pass an argument inside that parentheses

def nameit():
	print("Hello!")
nameit()
#passing parameter


def nameit(name):#parameter can be of anyname
	print("Hello!" + name)
nameit("Sudarshan")#if not passed we get an error

#passing 2 parameter

def nameit(fname,lname):#parameter can be of anyname
	print("Hello!" + fname + " " + lname)
nameit("Sudarshan","Hadadi Ramakrishna")


def mathit(num1,num2):#parameter can be of anyname
	print(num1 + num2)
mathit(10,32)

#return 

def mathit(num1,num2):#parameter can be of anyname
	return(num1 + num2)

print(mathit(10,32))#or we can assign to something
outcome = mathit(20,2000)#assigning
print(outcome)

#end of clASS 22
