#DESAFIO 8
# Faça um programa que leia via linha de comando três números e mostre-os em ordem decrescente.

import sys

lista = []

for i in range(3):
  lista.append(int(sys.argv[1]))
  lista.append(int(sys.argv[2]))
  lista.append(int(sys.argv[3]))

lista.sort(reverse=True)
print(lista)