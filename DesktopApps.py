from tkinter import *
import os 
os.system('clear')

#Thinter GUI

root = Tk()
root.title('Your Info ')
root.geometry("400x400")

#defining a func to do something 
def hello():
	hello_label = Label(root,text="Hello " + myTextbox.get())#calling myTextbox here gives the data entered 
	hello_label.pack()

#creating a label
myLabel = Label(root,text = "Enter your first name:")
myLabel.pack()

#creating text box so that we can enter our name 
myTextbox = Entry(root,width = 30)
myTextbox.pack() 

#Creating button 
myButton = Button(root,text="Submit",command=hello)#hello is function that is called here to do something
myButton.pack()




root.mainloop()