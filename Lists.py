import os
os.system('clear')

names = ["Sudarshan", "Parvathi","Santhosh"]
print(names[0])
print(names)
 
#Can change them 

names = ["Sudarshan", "Parvathi","Santhosh"]
names[0] = "Darshan"
print(names[0])
print(names)
 
# to add a value to the lists .....we can use append()

names = ["Sudarshan", "Parvathi","Santhosh"]
names.append("Sumanth")
print(names[3])
print(names)

#can add number to the same lists ...

names = ["Sudarshan", "Parvathi","Santhosh",42]
print(names[3])
print(names)

names = ["Sudarshan", "Parvathi","Santhosh",42]
print(names[3] + 10)
print(names)

# add variables to the lists

other_name = "Sumanth"
names = ["Sudarshan", "Parvathi","Santhosh",other_name]
print(names[0])
print(names)

#Can add other lists to the same lists

nums = [300,200,300]
names = ["Sudarshan", "Parvathi","Santhosh",nums]
print(names[3])
print(names[3][2]) #to get a number from the list nums 
print(names[3][2] + 100)#can add the numbersto the list value
print(names)

#when we have a lengthy lists and dont know how many are there in the lists,  we use len()...we also use this to find the last value of the lists

names = ["Sudarshan", "Parvathi","Santhosh"]
print(len(names))
print(names)
print(names[len(names)-1])#-1 coz the lists name starts with 0 

#end of class 11
