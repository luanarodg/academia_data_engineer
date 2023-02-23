# Exercicio 1
# Faça um programa que peça dois números via linha de comando e imprima o maior deles

import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

if num1 > num2:
  print(num1)
else:
  print(num2)