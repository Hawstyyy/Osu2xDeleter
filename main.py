import os
from tkinter import filedialog, ttk,messagebox
from tkinter import *

arquivos = []

def diretorio():
  global path
  path = filedialog.askdirectory()
  path_label.config(text=path)

def delete():
  for arquivo in os.listdir(path):
    if "@2x" in arquivo:
      os.remove(f'{path}/{arquivo}')
  messagebox.showinfo("Popup", "All @2x deleted!") 

def menu():
  for arquivo in os.listdir(path):
    if "@2x" in arquivo:
      arquivos.append(arquivo)

  if len(arquivos) == 0:
    messagebox.showinfo("Popup", "No @2x found") 

  else:
    mensagem = messagebox.askquestion("askquestion", f"{len(arquivos)} files will be erased, are you sure?")
    if mensagem:
      delete()

root = Tk()

root.geometry("500x300")
root.resizable(False, False)

ttk.Label(root, text="Selected folder:", font=("Arial", 20, "bold")).place(relx=0.5, rely=0.3, anchor=CENTER)
path_label = ttk.Label(root, font=("Arial", 12))
path_label.place(relx=0.5, rely=0.4, anchor=CENTER)

btn1 = Button(root, text="Select folder", command=diretorio, height=2, width=20)
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)

btn2 = Button(root, text="Delete @2x", command=menu, height=2, width=20)
btn2.place(relx=0.5, rely=0.75, anchor=CENTER)

root.mainloop()