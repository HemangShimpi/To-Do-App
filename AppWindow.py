'''
    File Name: LoginPage.py
    Author: Hemang Shimpi
    Date Created: 12/19/20
    Date last modified: 12/25/20
    Language: Python 
    Gui: Tkinter
'''

# importing all the necessary tkinter gui modules here
from tkinter import *
from tkinter import ttk, messagebox, Frame 
from tkinter.ttk import Combobox, Style

# importing cursor from mysql.connector here
from mysql.connector import cursor

# importing all necessary modules for sending emails, connecting to databses, and checking/verifying emails here
import re, mysql.connector, smtplib

# passing TopLevel to specify that a tkinter TopLevel window has been run for the compiler
class AppWindow(Toplevel):
    
    # __init__ constructor with *args and **kwargs
    def __init__(self, master=None, *args, **kwargs):

        # initiailizing tkinter Frame with parent and *args and **kwargs
        Frame.__init__(self, master, *args, **kwargs)

        # setting self.parent equal to parent
        self.master = master

        # running non-getter and setter class methods here 
        self.labels()
        self.buttons()
        self.entries()
        self.numOfTasks = 0
        
    # labels class method
    def labels(self):
        
        # creating all Labels in the AppWindow window here
        self.emailLbl = Label(self.master, text="Enter your email where we can remind you of your TO-DOs", font=("Roboto", 13), bg="#2a2a2a", fg="white")

        # placing the label using x and y coordinates and center anchor
        self.emailLbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    # emailBtnAction class method
    def emailBtnAction(self):

        # using the get method to get user input entry and setting it equal to the userEmail var 
        self.userEmail = str(self.emailEntry.get())
        
        # regex default key that checks if an email is valid or not
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        # conditional using re.search method and regex key for validation of email 
        if (re.search(regex, self.userEmail)):

            # message box for email validation success 
            messagebox.showinfo("Success!", ("Thanks! we will send you reminders of your To-Dos to this email:\n" + self.userEmail))

            # running secondPage method here 
            self.secondPage()

            # using destroy method to destroy (close) tkinter elements such as label, button, and entry      
            self.emailEntry.destroy()
            self.emailLbl.destroy()
            self.emailBtn.destroy()

        else:

            # messagebox for error for invalid email 
            messagebox.showerror("Error!", "Please enter a valid email address.")
    
    # buttons method
    def buttons(self):

        # creating all buttons in the AppWindow window here
        self.emailBtn = Button(self.master, text="Submit", font=("Roboto", 11), command=self.emailBtnAction)

        # placing emailBtn using x and y coordinates and center anchor
        self.emailBtn.place(relx=0.7, rely=0.6, anchor=CENTER)
        
    # entries method
    def entries(self):

        # creating all entries in the AppWindow window here
        self.emailEntry = Entry(self.master, width=30, bd=4, relief=SUNKEN)

        # placing emailEntry using x and y coordinates and center anchor
        self.emailEntry.place(relx=0.4, rely=0.6, anchor=CENTER)
    
    # secondPage method that consists of labels, entries, scrollbars, and listboxes
    def secondPage(self):

        # creating Label for tasks title
        self.tasksLbl = Label(self.master, text="Tasks", font=("Roboto", 25), bg="#2a2a2a", fg="white")

        # placing tasksLbl using x and y coordinates and center anchor
        self.tasksLbl.place(x=110,y=35,width=125)

        # creating listbox for list of tasks
        self.taskbox = Listbox(self.master, bd=3, font=("Roboto", 15), justify=CENTER)

        # placing taskbox using x and y coordinates and center anchor
        self.taskbox.place(x=20, y=80, width=320, height=250)
        
        # creating scrollbar for listbox
        self.scroll = Scrollbar(self.taskbox, command=self.taskbox.yview)

        # using pack to set side and fill for scrollbar
        self.scroll.pack(side=RIGHT, fill=BOTH)
        
        # configuration for taskbox to use the scrollbar to move in y direction
        self.taskbox.config(yscrollcommand=self.scroll.set)

        # Label for user direction (Enter Task: )
        self.enterTaskLbl = Label(self.master, text="Enter Task:", font=("Roboto", 13), bg="#2a2a2a", fg="white")

        # placing enterTasksLbl using x and y coordinates and center anchor
        self.enterTaskLbl.place(x=20,y=350,width=90,height=30)

        # Entry for user input of tasks
        self.taskEntry = Entry(self.master, bd=5)

        # placing taskEntry using x and y coordinates and center anchor
        self.taskEntry.place(x=110,y=350,width=230,height=30)
        
        # creating buttons in AppWindow here 
        self.addBtn = Button(self.master, text="Add Task", font=("Roboto", 13), width=13, height=2, command=self.addTask)
        self.addBtn.place(x=370,y=80,width=140,height=47)
        
        self.saveBtn = Button(self.master, text="Save Tasks", font=("Roboto", 13), width=13, height=2, command=self.saveTasks)
        self.saveBtn.place(x=370,y=170,width=140,height=47)
        
        self.loadBtn = Button(self.master, text="Update Tasks", font=("Roboto", 13), width=13, height=2, command=self.updateTask)
        self.loadBtn.place(x=370,y=260,width=140,height=47)

        self.removeBtn = Button(self.master, text="Delete Task", font=("Roboto", 13), width=13, height=2, command=self.removeTask)
        self.removeBtn.place(x=370,y=340,width=140,height=47)

    # addTask method for addBtn button to add tasks to listbox 
    def addTask(self):
        
        # using get method to get user input from task entry 
        self.taskName = self.taskEntry.get()

        # using insert method to insert value into listbox 
        self.taskbox.insert(END, self.taskName)

    # saveTasks method for saveBtn to save tasks of listbox
    def saveTasks(self):

        # setting tasksText variable to an empty list to fill in values later
        tasksText = []
        
        # conditional for empty input values
        if (self.taskName == ""):

            # messagebox to display error
            messagebox.showerror("Error!", ("Task cannot be empty\nPlease enter a task"))

        else:
            # concatenating taskbox items to tasksText var
            tasksText += [self.taskbox.get(0, self.taskbox.size())]

            # running sendEmailToRecipient method here to send email to user
            self.sendEmailToRecipient()
            
        
        # messagebox to display acknowledgement to user
        messagebox.showinfo("Tasks saved and reminder sent to your email ")       
        
    # removeTask method for removeBtn to remove tasks from listbox
    def removeTask(self):

        # setting selection var equal to cursor selection of an item from the listbox
        selection = self.taskbox.curselection()

        # using delete method to delete the value of selection var
        self.taskbox.delete(selection)

        # messagebox to display acknowledgement of deletion
        messagebox.showinfo("Deleted", "Task Deleted")

    # updateTask method for updateBtn to update task in the listbox
    def updateTask(self):

        # setting selection var to cursor selection of an item from the listbox
        selection = self.taskbox.curselection()

        # conditional for empty entry values
        if (self.taskEntry.get() == ""):

            # messagebox to display extra directions
            messagebox.showinfo("Update A Task", "Select a Task from the list by clicking on it and type the updated task in the entry box and click the update task button to finish updating your task")
        
        # elif for no cursor selection made from the user in the listbox
        elif (self.taskbox.get(ANCHOR) == ""):
            
            # messagebox to display extra directions
            messagebox.showinfo("Update A Task", "Please select a task to update")

        else:

            # using delete method to delete selection and replacing with new task
            self.taskbox.delete(selection)
            self.taskbox.insert(selection, self.taskEntry.get())
              
    # sending emails method
    def sendEmailToRecipient(self):

        # connection to MySQL database 
        db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="poonam@2815",
                database="todo"
        )

        # cursor for sql command executions
        cursor = db.cursor()

        # using truncate table to empty tasks column
        cursor.execute("TRUNCATE TABLE taskinfo")

        # using variables for sql command and variables for values
        data = "INSERT INTO taskinfo (task, email) VALUES (%s, %s)"
        values = (str(self.taskName), str(self.userEmail))

        # executing sql command using data and values variables
        cursor.execute(data, values)

        # using commit method to confirm execution
        db.commit()
        
        # executing select sql command 
        cursor.execute("SELECT task from taskinfo")

        # setting tasks var equal to data from fetchall of tasks column
        tasks = cursor.fetchall()

        # using commit method to confirm execution
        db.commit()

        # using SMTPLIB to send emails to users
        sendEmail = smtplib.SMTP("smtp.gmail.com", 587)

        # starttls method used to establish secure connection 
        sendEmail.starttls()

        # login and pass passed in using login method
        sendEmail.login("hemangshimpi2@gmail.com", "Hemang@281511")

        # emailSubject var for subject
        emailSubject = str("Tasks Reminder!")

        # emailBody var for body using string formatting 
        emailBody = str("This is a reminder of your tasks.\nTasks:{}".format(str(tasks)))

        # using string formatting for email construction
        email1 = f'Subject: {emailSubject}\n\n{emailBody}'

        # using sendmail method to send mail to designated recipient's email
        sendEmail.sendmail("hemangshimpi2@gmail.com", self.userEmail, email1)

        # using quit method to quit server
        sendEmail.quit()


# end of program

    








        
       

           
