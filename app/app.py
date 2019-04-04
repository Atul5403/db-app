#!/usr/local/bin/python3
from tkinter import *
from tkinter import ttk
import backend
  
class App(Tk):
    def __init__(self,*args,**kwargs):
    	Tk.__init__(self,*args,**kwargs)
    	self.notebook = ttk.Notebook()
    	self.title("EXPENSE MANAGER")
    	self.geometry("800x500")
    	self.add_tab()
    	self.notebook.grid(row=0)


    def add_tab(self):
    	tab = StartPage(self.notebook)
    	tab2 = PageOne(self.notebook)
    	self.notebook.add(tab,text="manage expense")
    	self.notebook.add(tab2,text="tag2")


class StartPage(Frame):
	def __init__(self,name,*args,**kwargs):
		Frame.__init__(self,*args,**kwargs)
		self.label = Label(self, text="Hi This is Tab1")
		self.label.grid(row=1,column=0,padx=10,pady=10)
		self.name = name


		def view_command():
			list1.delete(0,END)
			for row in backend.view():
				list1.insert(END,row)
			print("fetched all data")
			if not e1.get() :
				summation_command()

		def search_command():
			list1.delete(0,END)
			for row in backend.search(Id_text.get(),Name_text.get(),Cost_text.get()):
				list1.insert(END,row)

		def add_command():
			if Name_text.get() and Cost_text.get():
				backend.insert(Name_text.get(),Cost_text.get())
				view_command()
				summation_command()

		def update_command():
			backend.update(Id_text.get(),Name_text.get(),Cost_text.get())
			view_command()
			summation_command()

		def delete_command():
			backend.delete(Id_text.get())
			view_command()
			summation_command()

		def summation_command():
			l3 = Label(self, text = backend.summation())
			l3.grid()

		def quit():
			global self
			self.destroy()

		l0 = Label(self, text = "ID")
		l0.grid(row = 3, column = 3)

		Id_text = StringVar()
		e0 = Entry(self,textvariable= Id_text,width = 10)
		#e1.grid(row = 0, column = 1,)
		e0.grid(row = 3, column = 5)

	#NAME PART
		l1 = Label(self,text = "Name")
        #l1.grid(row = 0,column = 2)
		l1.grid(row = 4, column = 3)
		Name_text = StringVar()
		e1 = Entry(self,textvariable= Name_text)
        #e1.grid(row = 0, column = 3)
		e1.grid(row = 4, column = 5)
    #COST PART
		l2 = Label(self,text = "Cost")
        #l1.grid(row = 0,column = 4)
		l2.grid(row = 5, column = 3)
		Cost_text = StringVar()
		e1 = Entry(self,textvariable= Cost_text)
		e1.grid(row = 5, column = 5)
    

#DISPLAY DATA
		list1 = Listbox(self, height = 6, width = 35)
		list1.grid()
		list1.grid(row = 7, column = 7,rowspan = 6, columnspan = 2)

		sb1 = Scrollbar(self)
		sb1.grid()
        #sb1.grid(row = 2, column = 2,rowspan=6)
		list1.configure(yscrollcommand = sb1.set)
		sb1.configure(command = list1.yview)

#SUMM PART
		e1.grid()
		l3 = Label(self,text = "NET")
        #l2.grid(row = 8, column = 0)
		l3.grid()


#ACTION BUTTONS
		b1 = Button(self,text = "View Figure", width = 12,command = view_command)
        # b1.grid(row = 2, column = 3)
		b1.grid(column = 40, row = 3, columnspan = 10,padx = 5)

		b2 = Button(self,text = "Search Figure", width = 12, command = search_command)
        # b2.grid(row = 3, column = 3)
		b2.grid(column = 40, row = 8, columnspan = 10)

		b3 = Button(self,text = "Add Figure", width = 12,command = add_command)
        # b3.grid(row = 4, column = 3)
		b3.grid(column = 40, row = 12, columnspan = 10)

		b4 = Button(self,text = "Update Figure", width = 12, command = update_command)
        # b4.grid(row = 5, column = 3)
		b4.grid(column = 40, row = 16, columnspan = 10)

		b5 = Button(self,text = "Delete Figure", width = 12, command = delete_command)
        # b5.grid(row = 6, column = 3)
		b5.grid(column = 40, row = 20, columnspan = 10)

		b6 = Button(self,text = "Close", width = 12,command=quit)
        # b6.grid(row = 7, column = 3)
		b6.grid(column = 40, row = 24, columnspan = 10)
		self.pack()

class PageOne(Frame):
   def __init__(self,name,*args,**kwargs):
       Frame.__init__(self,*args,**kwargs)
       self.label = Label(self, text="Hi This is Tab2")
       self.label.grid(row=1,column=0,padx=10,pady=10)
       self.name = name
  
my_app = App()
my_app.mainloop()