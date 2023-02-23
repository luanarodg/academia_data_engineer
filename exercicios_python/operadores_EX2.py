#Exercício 2
#Faça um programa que peça via linha de comando as 4 notas bimestrais e mostre a média.

import sys

num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]
num4 = sys.argv[4]

media = (int(num1) + int(num2) + int(num3) + int(num4)) / 4

print(media)