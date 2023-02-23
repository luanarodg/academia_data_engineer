#Exercicio 5
# Faça um programa que leia um número via input de usuário e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.). Para valores negativos ou maiores que 7 exibir a mensagem "valor inválido"

numero_dia = int(input("Digite um número: "))

if numero_dia == 1:
  print("domingo")
elif numero_dia == 2:
  print("segunda")
elif numero_dia == 3:
  print('terça')
elif numero_dia == 4:
  print('quarta')
elif numero_dia == 5:
  print('quinta')
elif numero_dia == 6:
  print('sexta')
elif numero_dia == 7:
  print('sábado')
else:
  print('valor inválido')