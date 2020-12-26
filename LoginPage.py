from tkinter import *
from tkinter import ttk
from tkinter import Frame, messagebox

from AppWindow import AppWindow

import mysql.connector

class LoginPage(Frame):
    
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.labels()
        self.entries()
        self.buttons()
    
    def labels(self):
        titleLbl = Label(self.parent, text="To-Do App", font=("Roboto", 27), fg="white", bg="#2a2a2a")
        titleLbl.pack(pady=(10, 0))

        loginLbl = Label(self.parent, text="Log In", font=("Roboto", 19, "italic", "bold", UNDERLINE), fg="white", bg="#2a2a2a")
        loginLbl.place(x=110, y=110, anchor=CENTER)

        userLbl = Label(self.parent, text="Username: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")
        userLbl.place(x=68, y=210, anchor=CENTER)

        passLbl = Label(self.parent, text="Password:  ", font=("Roboto", 13), fg="white", bg="#2a2a2a")
        passLbl.place(x=68, y=250, anchor=CENTER)

        signUpLbl = Label(self.parent, text="Sign Up", font=("Roboto", 20, "italic", "bold", UNDERLINE), fg="white", bg="#2a2a2a")
        signUpLbl.place(x=380, y=110, anchor=CENTER)

        setNameLbl = Label(self.parent, text="Set Name: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")
        setNameLbl.place(x=305, y=170, anchor=CENTER)

        setAgeLbl = Label(self.parent, text="Set Age: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")
        setAgeLbl.place(x=297, y=210, anchor=CENTER)

        setUserLbl = Label(self.parent, text="Set Username: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")
        setUserLbl.place(x=320, y=250, anchor=CENTER)

        signUpLbl = Label(self.parent, text="Set Password: ", font=("Roboto", 13), fg="white", bg="#2a2a2a")
        signUpLbl.place(x=318, y=290, anchor=CENTER)
    
    def entries(self):
        self.usernameEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3)
        self.usernameEntry.place(x=160, y=211, anchor=CENTER)

        self.passwordEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3, show="*")
        self.passwordEntry.place(x=160, y=250, anchor=CENTER)

        self.nameEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3)
        self.nameEntry.place(x=430, y=171, anchor=CENTER)

        self.ageEntry = Entry(self.parent, width=15, relief=SUNKEN, bd=3)
        self.ageEntry.place(x=430, y=210, anchor=CENTER)

        self.setUser = Entry(self.parent, width=15, relief=SUNKEN, bd=3)
        self.setUser.place(x=430, y=250, anchor=CENTER)

        self.setPass = Entry(self.parent, width=15, relief=SUNKEN, bd=3)
        self.setPass.place(x=430, y=290, anchor=CENTER)

    def logInBtn(self):

        self.user = self.usernameEntry.get()
        self.passwd = self.passwordEntry.get()

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="poonam@2815",
            database="accountValues"
        )

        cursor = db.cursor()
        
        
        def sql():
            cursor.execute("SELECT * FROM UserInfo WHERE username=%s and password=%s", (str(self.user), str(self.passwd)))
            return cursor.fetchall()
        
        def destroyItems():
            self.destroy()
            self.parent.destroy()
        
        if (self.user == "" or self.passwd == ""):
            messagebox.showerror("Error!", "All fields are required!")
        else:
            validate = sql()
            if validate:
                db.close()
                destroyItems()
                
                try:
                    window_2 = Tk()
                    window_2.resizable(0,0)
                    window_2.title("To-Do Application")
                    window_2.geometry("530x400+400+150")
                    bg_img = PhotoImage(file="C:\\Users\\heman\\OneDrive\\Desktop\\Junior Year Documents\\PC_Club Project\\bg_img_2.png")
                    bg_lbl = Label(window_2, image=bg_img)
                    bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)
                    def thanks():
                        messagebox.showinfo("Goodbye! ", "Thanks for using my app!")
                        window_2.destroy()

                    window_2.protocol("WM_DELETE_WINDOW", thanks)
                    AppWindow(window_2)
                    window_2.mainloop()

                except AttributeError:
                    pass
            else:
                messagebox.showerror("Error!", "Invalid Username and Password")
                
    
    def signUpBtn(self):
        self.setUsername = str(self.setUser.get())
        self.setPasswd = str(self.setPass.get())
        self.setName = str(self.nameEntry.get())

        try:
            self.setAge = int(self.ageEntry.get())
        except ValueError:
            messagebox.showerror("Error!", "Please enter a number")
     

        if (self.setUsername == "" or self.setPasswd == "" or self.setName == "" or self.setAge == ""):
            messagebox.showerror("Error!", "All fields are required!")
        else:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="poonam@2815",
                database="accountValues"
            )

            cursor = db.cursor()
            
            data = "INSERT INTO userinfo (name, age, username, password) VALUES (%s, %s, %s, %s)"
            values = (self.setName, self.setAge, self.setUsername, self.setPasswd)

            cursor.execute(data, values)

            db.commit()

            db.close()

            self.nameEntry.delete(0, END)
            self.ageEntry.delete(0, END)
            self.setUser.delete(0, END)
            self.setPass.delete(0, END)

            self.nameEntry['state'] = DISABLED
            self.ageEntry['state'] = DISABLED
            self.setUser['state'] = DISABLED
            self.setPass['state'] = DISABLED

            messagebox.showinfo("Success!", "\t         Account created!\n\nLogin with your username and password to proceed")

    def buttons(self):
        submitBtn = Button(self.parent, text="Submit", font=("Roboto", 12), command=self.logInBtn, width=10)
        submitBtn.place(x=110, y=340, anchor=CENTER)
        
        submitBtn_2 = Button(self.parent, text="Submit", font=("Roboto", 12), command=self.signUpBtn, width=10)
        submitBtn_2.place(x=380, y=340, anchor=CENTER)
    
    