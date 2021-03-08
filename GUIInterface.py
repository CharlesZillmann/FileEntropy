###########################################################################################################
###########################################################################################################
# File: GUIInterface
# Description:
###########################################################################################################
###########################################################################################################
import tkinter as tk

###########################################################################################################
# Name: showGUI
# Parameters:
###########################################################################################################
def showGUI():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
    canvas1.pack()

    label1 = tk.Label(root, text='Calculate the Square Root')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    label2 = tk.Label(root, text='Type your Number:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label2)

    entry1 = tk.Entry(root)
    canvas1.create_window(200, 140, window=entry1)


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
    canvas1.create_window(200, 180, window=button1)

    root.mainloop()


