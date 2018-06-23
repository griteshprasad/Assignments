##1.Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter import *

root = Tk()
root.geometry("1600x800")
root.title("Assignment")

def root_exit():
    root.destroy()

def show_text():
    l2 = Label(f1,font = ("Algerian",30), text = "Did you clicked that button")
    l2.grid()

f1 = Frame(root)
f1.pack(side = TOP)

l1 = Label(f1,font = ("Algerian",20), text = "Hello World")
l1.grid()

b1 = Button(f1,font = "Arial", text = "Exit",command = root_exit)
b1.grid()


##2.Write a python program to in the same interface as above and  create a action when the button is click it will
##  display some text.

b2 = Button(f1,font = "Arial", text = "Click Here",command = show_text)
b2.grid()


##3.Create a frame using tkinter with any label text and two buttons.One to  exit and other to change the label to
##  some other text.

f2 = Frame(root)
f2.pack()

flag = 0

def change_text():
    global flag
    if flag == 0:
        l3.config(text = "Now You Don't")
        flag = 1
    else:
        l3.config(text = "Now You See Me")
        flag = 0
    

l3 = Label(f2,font = ("Helvetica",20),text = "Now You See Me")
l3.grid()

b3 = Button(f2,text = "Don't click", command = change_text)
b3.grid()
b4 = Button(f2, text = "End your life", command = root_exit)
b4.grid()

##4.Write a python program using tkinter interface to take an input in the GUI program and print it.

def change_it():
    text_variable = e1.get()
    l5 = Label(f2,font = ("Helvetica",30),text = text_variable)
    l5.grid()

l4 = Label(f2,font = ("Helvetica",30),text = "Enter Whatever you want : ")
l4.grid(row = 5,column = 0)

e1 = Entry(f2)
e1.grid(row = 5, column = 1)

b5 = Button(f2,text = "See Magic", command = change_it)
b5.grid()

root.mainloop
























