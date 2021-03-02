# Program: passwordstorage.py
# Author: Jacob Storer
# Last Reviewed: 03/01/2021
################
# Known Issues
# 1.) When you delete a row, and try to add a new one... logic isn't currently smart enough to handle incrementing to the next available UNIQUE ID value within database.
#    -- Potential fix is to insert some validation on the database side.
#    -- Or clear the text fields after every interaction with the buttons.
################
# Notes
# * Current structure of code doesn't save the database values when application restarts. Set up this way on purpose for use case testing.
################

# Libraries
from tkinter import *
from tkinter import ttk

# Initializations
window = Tk()
window.wm_title('Password Storage')
#window.geometry('1200x800')
window.resizable(False, False)

# Welcome message for CLI users
print('Welcome to the program "Password Storage".')

# Construct Database
import database

# Event Triggered Functions
def get_selected_row(event):
    print("Treeview selected")
    global cur_selection 
    try:
        txt = tv.item(tv.selection())['values']
        cur_selection = txt[0]
        e1.delete(0, END)
        e1.insert(END,txt[1]) 
        e2.delete(0, END)
        e2.insert(END,txt[2]) 
        e3.delete(0, END)
        e3.insert(END,txt[3]) 
        e4.delete(0, END)
        e4.insert(END,txt[4])  
        e5.delete(0, END)
        e5.insert(END,txt[5]) 
        e6.delete(0, END)
        e6.insert(END,txt[6]) 
        e7.delete(0, END)
        e7.insert(END,txt[7]) 
        e8.delete(0, END)
        e8.insert(END,txt[8])

    except IndexError:
        print('Treeview empty')
        cur_selection = "null"
        pass
 
# Button Triggered Functions
def view_all():
    print("view_all")
    # Clear TreeView
    for row in tv.get_children():
        tv.delete(row)

    # Display values matching search criteria
    loopcnt = 0
    for r in database.view_query_all():
        print(r)
        tv.insert("", 'end', text ="L" +str(loopcnt),  
             values =(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        loopcnt = loopcnt + 1

# Buttons
def search_entry():
    print("search_entry")
    # Clear TreeView
    for row in tv.get_children():
        tv.delete(row)
    print(search_text.get())

    # Display values matching search criteria
    loopcnt = 0
    for r in database.view_query(search_text.get()):
        print(r)
        tv.insert("", 'end', text ="L" +str(loopcnt),  
             values =(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        loopcnt = loopcnt + 1

def new_entry():
    print("new_entry")
    elementcnt = 1
    for row in tv.get_children():
        elementcnt = elementcnt + 1
    
    database.insert_row(elementcnt, website_text.get(), username_text.get(), password_text.get(), email_text.get(), company_text.get(), security1_text.get(), security2_text.get(), security3_text.get())
    view_all()

def update_selected():
    print("update_selected")
    if cur_selection == "null":
        return

    database.update_row(cur_selection, website_text.get(), username_text.get(), password_text.get(), email_text.get(), company_text.get(), security1_text.get(), security2_text.get(), security3_text.get())
    view_all()

def delete_selected():
    print("delete_selected")
    database.delete_row(cur_selection)
    view_all()

# Initialize User Input Labels
label1 = Label(window, text='Website')
label1.grid(row=0, column=0)

label2 = Label(window, text='Username')
label2.grid(row=1, column=0)

label3 = Label(window, text='Password')
label3.grid(row=2, column=0)

label4 = Label(window, text='E-mail')
label4.grid(row=3, column=0)

label5 = Label(window, text='Company')
label5.grid(row=0, column=2)

label6 = Label(window, text='Security #1')
label6.grid(row=1, column=2)

label7 = Label(window, text='Security #2')
label7.grid(row=2, column=2)

label8 = Label(window, text='Security #3')
label8.grid(row=3, column=2)

# Initialize User Input Fields
website_text = StringVar() # Creates spacial object
e1 = Entry(window, textvariable=website_text)
e1.grid(row=0, column=1)

username_text = StringVar() # Creates spacial object
e2 = Entry(window, textvariable=username_text)
e2.grid(row=1, column=1)

password_text = StringVar() # Creates spacial object
e3 = Entry(window, textvariable=password_text)
e3.grid(row=2, column=1)

email_text = StringVar() # Creates spacial object
e4 = Entry(window, textvariable=email_text)
e4.grid(row=3, column=1)

company_text = StringVar() # Creates spacial object
e5 = Entry(window, textvariable=company_text)
e5.grid(row=0, column=4)

security1_text = StringVar() # Creates spacial object
e6 = Entry(window, textvariable=security1_text)
e6.grid(row=1, column=4)

security2_text = StringVar() # Creates spacial object
e7 = Entry(window, textvariable=security2_text)
e7.grid(row=2, column=4)

security3_text = StringVar() # Creates spacial object
e8 = Entry(window, textvariable=security3_text)
e8.grid(row=3, column=4)

search_text = StringVar() # Creates spacial object
e9 = Entry(window, textvariable=search_text)
e9.grid(row=2, column=16)

# tkinter stlyin'
style = ttk.Style(window)
style.theme_use("clam") # set ttk theme to "clam" which supports the fieldbackground option
style.configure("Treeview", background="black", fieldbackground="teal", foreground="white")
tv = ttk.Treeview(window, columns=(1,2,3,4,5,6,7,8,9), show="headings", height="16", selectmode="browse", padding=15)
tv.bind('<<TreeviewSelect>>', get_selected_row)
tv.grid(row=5, column=0, rowspan=2, columnspan=20)
tv.heading(1, text='Id')
tv.heading(2, text='Website')
tv.heading(3, text='Username')
tv.heading(4, text='Password')
tv.heading(5, text='E-mail')
tv.heading(6, text='Company')
tv.heading(7, text='Security #1')
tv.heading(8, text='Security #2')
tv.heading(9, text='Security #3')

# Initialize Buttons
b1 = Button(window, text='View All', width=12, command=view_all)
b1.grid(row=1, column=5)

b2 = Button(window, text='Search Entry', width=12, command=search_entry)
b2.grid(row=1, column=16)

b3 = Button(window, text='New Entry', width=12, command=new_entry)
b3.grid(row=1, column=7)

b4 = Button(window, text='Update Selected', width=12, command=update_selected)
b4.grid(row=3, column=7)

b4 = Button(window, text='Delete Selected', width=12, command=delete_selected)
b4.grid(row=1, column=9)

b5 = Button(window, text='Exit Program', width=12, command=window.destroy)
b5.grid(row=3, column=9)

# Application Footer
label9 = Label(window, text="Password Storage -- Made with tkinter and Python -- Release v0.1 (BETA)")
label9.grid(row=17, column=0, columnspan=20)

# Main Body
window.mainloop() # Start program
