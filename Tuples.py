import os
os.system('clear')

names =("Sudarshan","Parvathi","Santhosh")
print(names)
print(names[0])

#we cant add or delete anything
#Tuples are faster than lists

tuple1 = ("Sudarshan","Parvathi","Santhosh")
tuple2 = ("Sumanth",)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 = ("Sudarshan","Parvathi","Santhosh")
tuple2 = ("Sumanth",)
print(tuple1[0:2])

tuple1 = ("Sudarshan","Parvathi","Santhosh")
tuple2 = ("Sumanth",)
tuple3 = tuple1[0]#[0:2] prints 1st 2 values
print(tuple3)

#end of class 12
