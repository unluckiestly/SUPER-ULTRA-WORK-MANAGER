from tkinter import *
from tkinter import ttk

b = Tk()
b.tk.call('source', 'forest-dark.tcl')

ttk.Style().theme_use('forest-dark')

button = ttk.Button(b, text="12345", style='Accent.TButton')
button.pack(pady=500, padx=100)


b.mainloop()
