import os
from tkinter import filedialog, ttk
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

def menu():
  for arquivo in os.listdir(path):
    if "@2x" in arquivo:
      arquivos.append(arquivo)

  if len(arquivos) == 0:
    top= Toplevel(root)
    top.geometry("200x100")
    top.resizable(False, False)
    top.title("Popup")

    Label(top, text= "@2x Not Found", font=("Arial", 12, "bold")).place(relx=0.5, rely=0.4, anchor=CENTER)
    Button(top, text= "Close", command=top.destroy, font=("Arial", 12)).place(relx=0.5, rely=0.7, anchor=CENTER)

  else:
    top= Toplevel(root)
    top.geometry("400x200")
    top.resizable(False, False)
    Label(top, text= f" {len(arquivos)} arquivos serão excluídos, tem certeza?", font=("Arial", 10, "bold")).place(relx=0.5, rely=0.4, anchor=CENTER)
    Button(top, text= "Sim", command=top.destroy, font=("Arial", 12)).place(relx=0.4, rely=0.7, anchor=CENTER)
    Button(top, text= "Cancelar", command=top.destroy, font=("Arial", 12)).place(relx=0.6, rely=0.7, anchor=CENTER)

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

