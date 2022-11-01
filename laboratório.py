import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry('300x100')

style = ttk.Style()

style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red', background='yellow')

btn1 = ttk.Button(root, text='Quit !', style='W.TButton', command=root.destroy)
btn1.grid(row=0, column=3, padx=100)

btn2 = ttk.Button(root, text='Click me !', command=None)
btn2.grid(row=1, column=3, pady=10, padx=100)

root.mainloop()
