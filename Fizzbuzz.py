import os
os.system('clear')

num = 0

while (num <= 100):
	if(num % 3 == 0) and (num % 5 == 0):
		print(str(num) + ": FIZZBUZZ!")
	elif(num % 3 == 0):
		print(str(num) + ": FIZZ!")
	elif(num % 5 == 0):
		print(str(num) + ": BUZZ!")
	else:
		print(str(num) + '.')
	num += 1

print("*******************************************************************************************")
#end of class 20
# to count how many fizz, buzz, fizzbuzz are there
print("Example for next class i.e class 21 ")

num = 0
fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0


while (num <= 100):
	if(num % 3 == 0) and (num % 5 == 0):
		print(str(num) + ": FIZZBUZZ!")
		fizzbuzzcount += 1

	elif(num % 3 == 0):
		print(str(num) + ": FIZZ!")
		fizzcount += 1

	elif(num % 5 == 0):
		print(str(num) + ": BUZZ!")
		buzzcount +=1

	else:
		print(str(num) + '.')
	num += 1

print("__________________________________________________________")
print("Fizz\tBuzz\tFizzBuzz")
print(str(fizzcount) + "\t" + str(buzzcount) + "\t" + str(fizzbuzzcount))
print(str("{:,}".format(fizzcount)) + "\t" + str("{:,}".format(buzzcount)) + "\t" + str("{:,}".format(fizzbuzzcount)))
#end of class 21
