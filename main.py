import os
import shutil as sh
from tkinter import *
from tkinter import filedialog
import tkinter as tk

def select_path():
  global path
  path = filedialog.askdirectory()

def apagar_2x():
  global path
  for arquivo in os.listdir(path):
    if "@2x" in arquivo:
      print(arquivo)
      os.remove(f'{path}/{arquivo}')

name = []
root = Tk()
root.title('Osu @2x Deleter')
root.geometry('400x200')
root.resizable(height=False, width=False)

button_path = tk.Button(root,
text='Select your folder',
command=select_path,
font=("Arial Bold", 12),
)

button_apagar = tk.Button(root,
text='Delete',
command=apagar_2x,
font=("Arial Bold", 12),
)

button_path.pack(side = LEFT)
button_apagar.pack(side = RIGHT)
root.mainloop()