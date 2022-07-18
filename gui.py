import tkinter as tk
from tkinter import filedialog 
from main import *


def openFile():
           
            filepath = filedialog.askopenfilename()
            file = open(filepath, 'r')

            
            file.close()

def main():
    window = tk.Tk()
    window.title('SFTP')
    greeting = tk.Label(text="SFTP program")
    window.geometry("600x500")
    greeting.pack()

    upload_button = tk.Button(
                text="Upload file", 
                command=openFile
                )

    upload_button.pack()

    window.mainloop()


if __name__ == "__main__":
    main()