from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from MainWindow import MainWindow


def main():

    window = Tk()
    window.resizable(0,0)
    window.title("To-Do Application")
    window.geometry("530x400+400+150")
    bg_img = PhotoImage(file="C:\\Users\\heman\\OneDrive\\Desktop\\Junior Year Documents\\PC_Club Project\\bg_img.png")
    bg_lbl = Label(window, image=bg_img)
    bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

    def thanks():
        messagebox.showinfo("Goodbye! ", "Thanks for using my app!")
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", thanks)
    MainWindow(window) 
    window.mainloop()  

if __name__ == "__main__":
    main()