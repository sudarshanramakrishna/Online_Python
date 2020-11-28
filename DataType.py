import os
os.system('clear')

# String .... Can be b/n double or single quotes

first_name = "Sudu"
print(first_name)

# Numbers...they are not wrapped in qotation marks...if so then they will be as strings  

age = 20
print(age)

# Lists ...grp of one thing ...can be strings, numbers, lists of lists,etc 

names =["Sudarshan","Parvathi","Santhosh"]
print(names[1]) # shld mention/select any one or else it shows syntax error
print(names) # prints entire lists 

# Tuples .......type of list that cant be alterned in any manner like add, delete,change etc 
# instead of sq brackets use normal one 

Names = ("Sudarshan","Parvathi","Santhosh","Sumanth")
print(Names)
print(Names[0])

# Dictionaries....grp of many things..made of 2 things ...1.key and 2 value pair

fav_chats = { 
              "Sudarshan": "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }
print(fav_chats)
print(fav_chats["Santhosh"])

# Boolean........ its either true or false
 
name = True 
print(name)

# end of class 6