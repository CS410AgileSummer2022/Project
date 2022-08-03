import tkinter as tk
from tkinter import *
from tkinter import filedialog 
from main import main as m


def openFile():
           
            filepath = filedialog.askopenfilename()
            file = open(filepath, 'r')
            file.close()

def login_info():
    m("login")

def main():
    window = tk.Tk()
    window.title('SFTP')
    greeting = tk.Label(text="SFTP program")
    window.geometry("600x500")
    greeting.pack()

    login_button = tk.Button(
        text="Connect to Remote",
        command=login_info
    )
    #upload_button = tk.Button(
    #            text="Upload file", 
    #            command=open_file
    #            )

    login_button.pack()
    #upload_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()