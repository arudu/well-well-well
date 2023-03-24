import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("200x200")
text_var = tk.StringVar()

spinval =tk.StringVar()
s = ttk.Spinbox(root, values=["apple", "bananas", "cherries", "pears"],textvariable=spinval)
s.pack()

spinval =tk.StringVar()
s = ttk.Spinbox(root, values=["cat", "dog", "rabbit", "rat"],textvariable=spinval)
s.pack()

button =tk.Button(root, text="Submit")
button.pack()

root.mainloop()
