from tkinter import *
from tkinter import ttk, messagebox, Frame 
from tkinter.ttk import Combobox, Style
from mysql.connector import cursor
from tkcalendar import DateEntry

import re, mysql.connector, smtplib, schedule, time

class AppWindow(Toplevel):
    
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.labels()
        self.buttons()
        self.entries()
        self.numOfTasks = 0
        


    def labels(self):

        self.emailLbl = Label(self.master, text="Enter your email where we can remind you of your TO-DOs", font=("Roboto", 13), bg="#2a2a2a", fg="white")
        self.emailLbl.place(relx=0.5, rely=0.5, anchor=CENTER)


    def emailBtnAction(self):

        self.userEmail = str(self.emailEntry.get())
        
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if (re.search(regex, self.userEmail)):
            messagebox.showinfo("Success!", ("Thanks! we will send you reminders of your To-Dos to this email:\n" + self.userEmail))
            self.secondPage()
                       
            self.emailEntry.destroy()
            self.emailLbl.destroy()
            self.emailBtn.destroy()

        else:
            messagebox.showerror("Error!", "Please enter a valid email address.")
    
    def buttons(self):
        self.emailBtn = Button(self.master, text="Submit", font=("Roboto", 11), command=self.emailBtnAction)
        self.emailBtn.place(relx=0.7, rely=0.6, anchor=CENTER)
        

    def entries(self):
        self.emailEntry = Entry(self.master, width=30, bd=4, relief=SUNKEN)
        self.emailEntry.place(relx=0.4, rely=0.6, anchor=CENTER)
    
    def secondPage(self):

        self.tasksLbl = Label(self.master, text="Tasks", font=("Roboto", 25), bg="#2a2a2a", fg="white")
        self.tasksLbl.place(x=110,y=35,width=125)

        self.taskbox = Listbox(self.master, bd=3, font=("Roboto", 15), justify=CENTER)
        self.taskbox.place(x=20, y=80, width=320, height=250)
        
        self.scroll = Scrollbar(self.taskbox, command=self.taskbox.yview)
        self.scroll.pack(side=RIGHT, fill=BOTH)
        
        self.taskbox.config(yscrollcommand=self.scroll.set)

        self.enterTaskLbl = Label(self.master, text="Enter Task:", font=("Roboto", 13), bg="#2a2a2a", fg="white")
        self.enterTaskLbl.place(x=20,y=350,width=90,height=30)
     
        self.taskEntry = Entry(self.master, bd=5)
        self.taskEntry.place(x=110,y=350,width=230,height=30)
        
        self.addBtn = Button(self.master, text="Add Task", font=("Roboto", 13), width=13, height=2, command=self.addTask)
        self.addBtn.place(x=370,y=80,width=140,height=47)
        
        self.saveBtn = Button(self.master, text="Save Tasks", font=("Roboto", 13), width=13, height=2, command=self.saveTasks)
        self.saveBtn.place(x=370,y=170,width=140,height=47)
        
        self.loadBtn = Button(self.master, text="Update Tasks", font=("Roboto", 13), width=13, height=2, command=self.updateTask)
        self.loadBtn.place(x=370,y=260,width=140,height=47)

        self.removeBtn = Button(self.master, text="Delete Task", font=("Roboto", 13), width=13, height=2, command=self.removeTask)
        self.removeBtn.place(x=370,y=340,width=140,height=47)

        
    def addTask(self):
        self.taskName = self.taskEntry.get()
        self.taskbox.insert(END, self.taskName)

    def saveTasks(self):

        tasksText = []
        
        if (self.taskName == ""):
            messagebox.showerror("Error!", ("Task cannot be empty\nPlease enter a task"))
        else:
            tasksText += [self.taskbox.get(0, self.taskbox.size())]
            self.sendEmailToRecipient()
            

        messagebox.showinfo("Here are your tasks", str(tasksText))       
        

    def removeTask(self):
        selection = self.taskbox.curselection()
        self.taskbox.delete(selection)
        messagebox.showinfo("Deleted", "Task Deleted")

    def updateTask(self):
        selection = self.taskbox.curselection()
        if (self.taskEntry.get() == ""):
            messagebox.showinfo("Update A Task", "Select a Task from the list by clicking on it and type the updated task in the entry box and click the update task button to finish updating your task")
        elif (self.taskbox.get(ANCHOR) == ""):
            messagebox.showinfo("Update A Task", "Please select a task to update")
        else:
            self.taskbox.delete(selection)
            self.taskbox.insert(selection, self.taskEntry.get())
              
    def sendEmailToRecipient(self):

        db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="poonam@2815",
                database="todo"
        )

        cursor = db.cursor()

        cursor.execute("TRUNCATE TABLE taskinfo")

        data = "INSERT INTO taskinfo (task, email) VALUES (%s, %s)"
        values = (str(self.taskName), str(self.userEmail))

        cursor.execute(data, values)

        db.commit()

        cursor.execute("SELECT task from taskinfo")
        tasks = cursor.fetchall()
        db.commit()

        sendEmail = smtplib.SMTP("smtp.gmail.com", 587)
        sendEmail.starttls()
        sendEmail.login("hemangshimpi2@gmail.com", "Hemang@281511")
        emailSubject = str("Tasks Reminder!")
        emailBody = str("This is a reminder of your tasks.\nTasks:{}".format(str(tasks)))
        email1 = f'Subject: {emailSubject}\n\n{emailBody}'
        sendEmail.sendmail("hemangshimpi2@gmail.com", self.userEmail, email1)
        sendEmail.quit()


    








        
       

           
