import tkinter as tk
from tkinter import *
from tkinter import filedialog 
from main import *


def openFile():
           
            filepath = filedialog.askopenfilename()
            file = open(filepath, 'r')

            
            file.close()

#def login_info():


def main():
    window = tk.Tk()
    window.title('SFTP')
    greeting = tk.Label(text="SFTP program")
    window.geometry("600x500")
    greeting.pack()

    L1 = tk.Label(window, text="User Name")
    L1.pack( fill = X)
    E1 = tk.Entry(window, bd =5)
    E1.pack( fill = X)

    #login_button = tk.Button(
    #    text="Log In",
        #command=login_info
    #)


    #upload_button = tk.Button(
    #            text="Upload file", 
    #            command=open_file
    #            )

    #login_button.pack()
    #upload_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()