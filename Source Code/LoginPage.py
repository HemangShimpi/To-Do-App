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
from tkinter import ttk
from tkinter import Frame, messagebox

# importing class here
from AppWindow import AppWindow

# importing mysql.connector for MySQL database connection
import mysql.connector

# passing Frame to specify that a tkinter Frame has been run for the compiler
class LoginPage(Frame):
    
    # __init__ constructor with *args and **kwargs
    def __init__(self, parent, *args, **kwargs):

        # initiailizing tkinter Frame with parent and *args and **kwargs
        Frame.__init__(self, parent, *args, **kwargs)

        # setting self.parent equal to parent
        self.parent = parent

        # running non-getter and setter class methods here 
        self.labels()
        self.entries()
        self.buttons()
    
    # labels class method
    def labels(self):

        # creating all Labels in the LoginPage window here
        titleLbl = Label(self.parent, text="To-Do App", font=("Roboto", 27), fg="white", bg="#2a2a2a")

        # y direction padding for styling the label
        titleLbl.pack(pady=(10, 0))

        loginLbl = Label(self.parent, text="Log In", font=("Roboto", 19, "italic", "bold", UNDERLINE), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        loginLbl.place(x=110, y=110, anchor=CENTER)

        userLbl = Label(self.parent, text="Username: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        userLbl.place(x=68, y=210, anchor=CENTER)

        passLbl = Label(self.parent, text="Password:  ", font=("Roboto", 13), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        passLbl.place(x=68, y=250, anchor=CENTER)

        signUpLbl = Label(self.parent, text="Sign Up", font=("Roboto", 20, "italic", "bold", UNDERLINE), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        signUpLbl.place(x=380, y=110, anchor=CENTER)

        setNameLbl = Label(self.parent, text="Set Name: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        setNameLbl.place(x=305, y=170, anchor=CENTER)

        setAgeLbl = Label(self.parent, text="Set Age: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        setAgeLbl.place(x=297, y=210, anchor=CENTER)

        setUserLbl = Label(self.parent, text="Set Username: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        setUserLbl.place(x=320, y=250, anchor=CENTER)

        signUpLbl = Label(self.parent, text="Set Password: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")

        # placing the label using x and y coordinates and center anchor
        signUpLbl.place(x=318, y=290, anchor=CENTER)
    

    # entries class method 
    def entries(self):

        # creating all user input entries in the LoginPage window here
        self.usernameEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3)

        # placing the label using x and y coordinates and center anchor
        self.usernameEntry.place(x=160, y=211, anchor=CENTER)

        self.passwordEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3, show="*")

        # placing the label using x and y coordinates and center anchor
        self.passwordEntry.place(x=160, y=250, anchor=CENTER)

        self.nameEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3)

        # placing the label using x and y coordinates and center anchor
        self.nameEntry.place(x=430, y=171, anchor=CENTER)

        self.ageEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3)

        # placing the label using x and y coordinates and center anchor
        self.ageEntry.place(x=430, y=210, anchor=CENTER)

        self.setUser = Entry(self.parent, width=15, relief=SUNKEN, bd=3)

        # placing the label using x and y coordinates and center anchor
        self.setUser.place(x=430, y=250, anchor=CENTER)

        self.setPass = Entry(self.parent, width=15, relief=SUNKEN, bd=3)

        # placing the label using x and y coordinates and center anchor
        self.setPass.place(x=430, y=290, anchor=CENTER)

    # loginBtn command method 
    def logInBtn(self):

        # using the get method to get user input from the entries and setting it equal to vars
        self.user = self.usernameEntry.get()
        self.passwd = self.passwordEntry.get()

        # connection to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dummyPass",
            database="accountValues"
        )

        # cursor to execute sql commands
        cursor = db.cursor()

        # sql method to verify username and password passed in the input entries        
        def sql():
            
            # cursor execute method
            cursor.execute("SELECT * FROM UserInfo WHERE username=%s and password=%s", (str(self.user), str(self.passwd)))

            # returns boolean true or false
            return cursor.fetchall()
        
        # destroyItems method to destroy window 
        def destroyItems():
            self.destroy()
            self.parent.destroy()
        
        # conditional for empty entries
        if (self.user == "" or self.passwd == ""):

            messagebox.showerror("Error!", "All fields are required!")

        else:

            validate = sql()
            
            # conditional for true or false outcomes
            if validate:

                # closes the db server connection 
                db.close()

                # running the destroyItems method here
                destroyItems()
                
                # try and except for AttributeError
                try:

                    # creating new window for App and modifying its elements such as title, window size, etc
                    window_2 = Tk()
                    window_2.resizable(0,0)
                    window_2.title("To-Do Application")
                    window_2.geometry("530x400+400+150")

                    # using PhotoImage to set a background image as a label for the window 
                    bg_img = PhotoImage(file="C:\\Desktop\\Junior Year Documents\\PC_Club Project\\bg_img_2.png")
                    bg_lbl = Label(window_2, image=bg_img)

                    # places the image directly in the center
                    bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

                    # creating thanks method here to thank the user for using the app by using tkinter messagebox
                    def thanks():

                        messagebox.showinfo("Goodbye! ", "Thanks for using my app!")

                        # destroys (closes) the window
                        window_2.destroy()

                    # using protocol method to run thanks method after user closes the window
                    window_2.protocol("WM_DELETE_WINDOW", thanks)

                    ''' passing window in the LoginPage class parameters to have it contain all elements that the class has '''
                    AppWindow(window_2)

                    # mainloop to run and end the window
                    window_2.mainloop()

                # except if AttributeError is caught during execution
                except AttributeError:
                    # pass key to continue the next script execution
                    pass
            else:
                
                # messagebox for invalid username and password
                messagebox.showerror("Error!", "Invalid Username and Password")
                
    # signUpBtn command method
    def signUpBtn(self):

        # using the get method to get user input from the entries and setting it equal to vars
        self.setUsername = str(self.setUser.get())
        self.setPasswd = str(self.setPass.get())
        self.setName = str(self.nameEntry.get())

        # try and except for ValueError
        try:
            # using the get method to get user input from entry and setting it equal to setAge var
            self.setAge = int(self.ageEntry.get())
        
        # except if ValueError is caught
        except ValueError:

            # messagebox for error
            messagebox.showerror("Error!", "Please enter a number")
     
        # conditional for empty entries
        if (self.setUsername == "" or self.setPasswd == "" or self.setName == "" or self.setAge == ""):
            messagebox.showerror("Error!", "All fields are required!")
        
        else:

            # connection to MySQL database
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="dummyPass",
                database="accountValues"
            )
            
            # cursor for executing sql commands
            cursor = db.cursor()

            # setting vars equal to sql commands and passing variables in as values       
            data = "INSERT INTO userinfo (name, age, username, password) VALUES (%s, %s, %s, %s)"
            values = (self.setName, self.setAge, self.setUsername, self.setPasswd)

            # executes sql command using data and values var
            cursor.execute(data, values)

            # commit to confirm execution and insertion 
            db.commit()
            
            # closes the db server connection
            db.close()

            # using delete method to clear entries 
            self.nameEntry.delete(0, END)
            self.ageEntry.delete(0, END)
            self.setUser.delete(0, END)
            self.setPass.delete(0, END)

            # setting state of entries to be disabled so it won't be editable anymore 
            self.nameEntry['state'] = DISABLED
            self.ageEntry['state'] = DISABLED
            self.setUser['state'] = DISABLED
            self.setPass['state'] = DISABLED

            # messagebox for successful account creation
            messagebox.showinfo("Success!", "\t         Account created!\n\nLogin with your username and password to proceed")

    # buttons method 
    def buttons(self):

        # creating all buttons for LoginPage window here
        submitBtn = Button(self.parent, text="Submit", font=("Roboto", 12), command=self.logInBtn, width=10)

        # placing button using x and y coordinates and center anchor
        submitBtn.place(x=110, y=340, anchor=CENTER)
        
        submitBtn_2 = Button(self.parent, text="Submit", font=("Roboto", 12), command=self.signUpBtn, width=10)

        # placing button using x and y coordinates and center anchor
        submitBtn_2.place(x=380, y=340, anchor=CENTER)

# end of program
    
