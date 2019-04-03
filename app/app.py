from tkinter import *
import backend
# Ctrl+ENTER to go to next line

def view_command():
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in backend.search(Name_text.get(),Cost_text.get()):
		list1.insert(END,row)

window = Tk()


l1 = Label(window,text = "Name")
l1.grid(row = 0,column = 0)

l1 = Label(window,text = "Cost")
l1.grid(row = 0,column = 2)

Name_text = StringVar()
e1 = Entry(window,textvariable= Name_text)
e1.grid(row = 0, column = 1)

Cost_text = StringVar()
e1 = Entry(window,textvariable= Cost_text)
e1.grid(row = 0, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0,rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2,rowspan=6)

list1.configure(yscrollcommand = sb1.set	)
sb1.configure(command = list1.yview)

b1 = Button(window,text = "View Figure", width = 12,command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window,text = "Search Figure", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window,text = "Add Figure", width = 12)
b3.grid(row = 4, column = 3)

b4 = Button(window,text = "Update Figure", width = 12)
b4.grid(row = 5, column = 3)

b5 = Button(window,text = "Delete Figure", width = 12)
b5.grid(row = 6, column = 3)

b6 = Button(window,text = "Close", width = 12)
b6.grid(row = 7, column = 3)


window.mainloop()