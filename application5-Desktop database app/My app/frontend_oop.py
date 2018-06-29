from tkinter import *
from backend_oop import Database

database=Database("books.db")

def get_selected_row(event):
	global selected_tuple
	index=listbox.curselection()[0]
	selected_tuple=listbox.get(index)
	e1.delete(0,END)
	e1.insert(END,selected_tuple[1])
	e2.delete(0,END)
	e2.insert(END,selected_tuple[2])
	e3.delete(0,END)
	e3.insert(END,selected_tuple[3])
	e4.delete(0,END)
	e4.insert(END,selected_tuple[4])
	
def view_command():
	listbox.delete(0,END)
	for row in database.view():
		listbox.insert(END,row)
def search_command():
	listbox.delete(0,END)
	for row in database.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
		listbox.insert(END,row)

def add_command():
	database.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
	listbox.delete(0,END)
	listbox.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))
	
def delete_command():
	database.delete(selected_tuple[0])

def update_command():
	database.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())

window=Tk()

window.wm_title("BookStore")
lb1=Label(window,text="Title")
lb1.grid(row=0,column=0)
title_value=StringVar()
e1=Entry(window,textvariable=title_value)
e1.grid(row=0,column=1)

lb2=Label(window,text="Author")
lb2.grid(row=0,column=2)
author_value=StringVar()
e2=Entry(window,textvariable=author_value)
e2.grid(row=0,column=3)

lb3=Label(window,text="Year")
lb3.grid(row=1,column=0)
year_value=StringVar()
e3=Entry(window,textvariable=year_value)
e3.grid(row=1,column=1)

lb4=Label(window,text="ISBN")
lb4.grid(row=1,column=2)
isbn_value=StringVar()
e4=Entry(window,textvariable=isbn_value)
e4.grid(row=1,column=3)

b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

listbox = Listbox(window, height=6,width=35)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()