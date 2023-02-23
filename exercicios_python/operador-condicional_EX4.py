#Exercício 4
# Faça um programa que leia três números e mostre o maior deles

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

if x > y and x > z:
  print(f"{x} é o maior número")
elif y > x and y > z:
  print(f"{y} é o maior número")
else:
  print(f"{z} é o maior número")