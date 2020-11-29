import os
import sqlite3
os.system('clear')
# bacis of sql
# we need to connect which is in back

#connect to dB

conn = sqlite3.connect('customer.db')#this doesnt exist here we havvent created it..python tries to connect autimatically..if it is not there u need to create a DB 

#create a cursor 
c =conn.cursor() 

#create the table
#executing   
'''
c.execute(""" CREATE TABLE customer( 
			fname text,
			lname text,
			email text
			)""")
'''
#Data added
#c.execute("INSERT INTO customer VALUES('Sudarshan','Ramakrishna','sudarshanramakrishna82@gmail.com')")

#print(" Data added ")

#pull the data that we added ..we do that by
c.execute("SELECT * FROM customer")

#to fetch

#print(c.fetchall()[0][0])#other option is just one time 0 and no zeros

items = c.fetchall()

for item in items:
	print(item[0] + " " + item[1])

#commit changes
conn.commit()

#close db connection
conn.close()

#end of class 24