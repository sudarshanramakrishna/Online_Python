import os
os.system('clear')
#made up of key and value pair 
#can write all in one line ...but it looks odd we make iot read comfortabaly to others
fav_chats = { 
              "Sudarshan": "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }

#prints all the values inside it 

print(fav_chats)

#prints the specific one that we choose 

print(fav_chats["Sudarshan"])

#to delete use del func

fav_chats = { 
              "Sudarshan": "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }

del fav_chats["Sudarshan"]
print(fav_chats)

#adding

fav_chats = { 
              "Sudarshan": "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }

fav_chats.update({"Vamshi": "Gobi Manchuri"})

print(fav_chats)
print(fav_chats["Vamshi"])

#to change the value

fav_chats = { 
              "Sudarshan": "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }
fav_chats["Parvathi"] = "Pani Puri"
print(fav_chats)
print(fav_chats["Parvathi"])
 
#can be anything(number,array etc)  and can use the same to call


fav_chats = { 
              42 : "Kabab",
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }
print(fav_chats)
print(fav_chats[42]) 

fav_chats = { 
              "Sudarshan" : [1,2,3,4],
              "Parvathi" : "Chicken Fry",
              "Santhosh" : "Chicken 65",
              "Sumanth"  : "Chicken Lolipop"	           
            }
print(fav_chats)
print(fav_chats["Sudarshan"][2]) 
print(fav_chats["Sudarshan"][2] + 7) 

#end of class 13
