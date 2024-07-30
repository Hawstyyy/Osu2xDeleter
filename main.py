import os
from tkinter import filedialog
import time

while True:
  arquivos = []
  path = filedialog.askdirectory()

  for arquivo in os.listdir(path):
    if "@2x" in arquivo:
      arquivos.append(arquivo)
  
  if len(arquivos) == 0:
    print("- Nenhum arquivos @2x encotrado")
    continue
  else:
    print('A seguinte quantidade de arquivos serão excluídos: ', len(arquivos))

    choice = input("Deixa mesmo continuar? (S/N) ").capitalize()

    if choice not in ['N','S']:
      print('Escolha inválida')
      continue

    elif choice == 'S':
      for arquivo in os.listdir(path):
        if "@2x" in arquivo:
          os.remove(f'{path}/{arquivo}')
      print("Encerrando")
      break

    elif choice == 'N':
      print('Cancelando...')
      time.sleep(2)
      break
