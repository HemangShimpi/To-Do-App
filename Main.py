'''
    File Name: Main.py
    Author: Hemang Shimpi
    Date Created: 12/19/20
    Date last modified: 12/25/20
    Language: Python 
    Gui: Tkinter
'''

# importing all the necessary tkinter gui modules here
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# importing class here
from LoginPage import LoginPage

# main method
def main():

    # creating tkinter window here and modifying its elements such as title, window size, etc
    window = Tk()
    window.resizable(0,0)
    window.title("To-Do Application")
    window.geometry("530x400+400+150")

    # using PhotoImage to set a background image as a label for the window 
    bg_img = PhotoImage(file="C:\\Users\\heman\\OneDrive\\Desktop\\Junior Year Documents\\PC_Club Project\\bg_img.png")
    bg_lbl = Label(window, image=bg_img)

    # places the image directly in the center
    bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

    # creating thanks method here to thank the user for using the app by using tkinter messagebox
    def thanks():
        messagebox.showinfo("Goodbye! ", "Thanks for using my app!")

        # destroys (closes) the window
        window.destroy()

    # using protocol method to run thanks method after user closes the window
    window.protocol("WM_DELETE_WINDOW", thanks)

    # passing window in the LoginPage class parameters to have it contain all elements that the class has
    LoginPage(window) 

    # mainloop to run and end the window
    window.mainloop()  

# if test 
if __name__ == "__main__":
    main()

# end of program