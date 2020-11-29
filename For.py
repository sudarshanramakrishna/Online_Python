import os
os.system('clear')

# used for itration

name = "Sudarshan"

# x(can be anything..and can be assigned to any value) is just place holder variable(like counter) that helps to itrate 

for x in name:
	print(x)

for apple in name:# as told x can be anything 
	print(apple)

names =["Sudarshan","Parvathi","Santhosh"]

for fname in names:
	print(fname)

fav_chats = { 
              "Sudarshan": "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            } #use of dictinories

for key,value in fav_chats.items():#in dict we should call .items() to get all the items in dictinaries
	print(key)

for key,value in fav_chats.items():#in dict we should call .items() to get all the items in dictinaries
	print(value)
	
for key,value in fav_chats.items():#in dict we should call .items() to get all the items in dictinaries
	print(key + " Likes " + value )
	
#end of class 19