import os
import shutil as sh
from tkinter import *
from tkinter import filedialog
import tkinter as tk

def select_pasta():
  path = filedialog.askdirectory()

# def apagar_2x():
#   for arquivo in os.walk(path):
#     if "@2x" in arquivo:
#       print(arquivo)
#       os.remove(f'{path}/{arquivo}')

name = []
root = Tk()
root.title('Osu @2x Deleter')
root.geometry('400x200')
root.resizable(height=False, width=False)

button_path = tk.Button(root,
text='Select your folder',
command=select_pasta
)
button_path.grid(padx=50,pady=100)
root.mainloop()
