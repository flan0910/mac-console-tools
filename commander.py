import sys
import tkinter as tk
import os
main = tk.Tk()
main.title("MacCommander v1.0")
main.geometry("200x100")

def Send(event):
    val = EditBox.get()
    if val == "sudo su":
       EditBox.delete(0, tk.END)
       return
    elif val == "su":
        EditBox.delete(0, tk.END)
        return
    elif val > "sudo ":
        EditBox.delete(0, tk.END)
        return
    elif val =="nano" and "vim":
          EditBox.delete(0, tk.END)
          return
    os.system(val)
    EditBox.delete(0, tk.END)

Static1 = tk.Label(text=u'CmdApp')
Static1.pack()

EditBox = tk.Entry(width=50)
EditBox.insert(tk.END,"")
EditBox.pack()

value = EditBox.get()


Button = tk.Button(text=u'Send')
Button.bind("<Button-1>",Send)
Button.pack()


main.mainloop()
