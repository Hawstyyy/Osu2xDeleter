import os
from tkinter import filedialog
import time

while True:
  path = filedialog.askdirectory()

  print(f'- Diretório Selecionado: {os.path.dirname(path)}')
  print('Os seguintes arquivos serão excluídos: ')

  for arquivo in os.listdir(path):
    if "@2x" in arquivo:
      print(arquivo)

  choice = input("Deixa mesmo continuar? (S/N) ").capitalize()

  if choice not in ['N','S']:
    print('Escolha inválida')

  elif choice == 'S':
    for arquivo in os.listdir(path):
      if "@2x" in arquivo:
        os.remove(f'{path}/{arquivo}')

  elif choice == 'N':
    print('Cancelando...')
    time.sleep(2)
    break
