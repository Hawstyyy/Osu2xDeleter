import os
import shutil as sh
from tkinter import *
from tkinter import filedialog

name = []
root = Tk()
root.withdraw()
path = filedialog.askdirectory()

for arquivo in os.listdir(path):
  name.append(arquivo)

print(name[1])

for arquivo in name:
  if ".png" in arquivo:
    print(arquivo)