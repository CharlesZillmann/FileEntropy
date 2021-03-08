###########################################################################################################
###########################################################################################################
# File: GUIInterface
# Description:
###########################################################################################################
###########################################################################################################
import tkinter as tk
from tkinter import filedialog
from tkinter import *

###########################################################################################################
# Name: askSourceDirectory
# Parameters:
###########################################################################################################
def askSourceDirectory():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

###########################################################################################################
# Name: showGUI
# Parameters:
###########################################################################################################
def showGUI():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=600, height=300, relief='raised')
    canvas1.pack()

    label1 = tk.Label(root, text='Organize Files')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(80, 20, window=label1)

    label2 = tk.Label(root, text='Source Directory to Organize:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(80, 70, window=label2)

    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=0, padx=10, pady=10, ipady=50)
    canvas1.create_window(100, 110, window=entry1)

    label3 = tk.Label(root, text='Destination Directory for Files:')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(80, 150, window=label3)

    entry2 = tk.Entry(root)
    entry2.grid(row=0, column=0, padx=10, pady=10, ipady=50)
    canvas1.create_window(100, 190, window=entry2)

    def getSquareRoot():
        x1 = entry1.get()
        if x1 == '':
            label3 = tk.Label(root, text='Please enter a value.', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)
        else:
            label3 = tk.Label(root, text='The Square Root of ' + x1 + ' is:', font=('helvetica', 10))
            canvas1.create_window(200, 210, window=label3)
            label4 = tk.Label(root, text=float(x1) ** 0.5, font=('helvetica', 10, 'bold'))
            canvas1.create_window(200, 230, window=label4)

    button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='blue', fg='black',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 240, window=button1)

    root.mainloop()



###########################################################################################################
###########################################################################################################
#                                             End File
###########################################################################################################
###########################################################################################################
