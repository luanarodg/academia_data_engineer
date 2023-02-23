#Exercício 4
#Faça um programa que peça via linha de comando o valor do tamanho do lado de um quadrado e faça o cálculo da área. Exiba o valor dessa área.

import sys

lado = sys.argv[1]

area  = int(lado)**2

print(f'Area: {lado} x {lado} = {area}cm²')