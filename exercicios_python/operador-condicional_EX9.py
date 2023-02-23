# DESAFIO 9
### Faça um programa que faça 5 perguntas para uma pessoa sobre um crime:
##### "Falou com a vítima no dia do crime?"
##### "Esteve no local do crime?"
##### "Mora perto da vítima?"
##### "Devia dinheiro para a vítima?"
##### "Já trabalhou com a vítima?"

### Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassina". Caso contrário, ela será classificada como "Inocente"


perg = []

print("Responda 1 para 'Sim' e 0 para 'Não'")

perg.append(input("\nFalou com a vítima no dia do crime? "))
perg.append(input("Esteve no local do crime? "))
perg.append(input("Mora perto da vítima? "))
perg.append(input("Devia dinheiro para a vítima? "))
perg.append(input("Já trabalhou com a vítima? "))

respostas = 0
for i in perg:
  respostas += int(i)

if respostas == 2:
  print('\nSuspeita')
elif respostas == 3 or respostas == 4:
  print("\nCúmplice")
elif respostas == 5:
  print("\nAssassina")
else:
  print("\nInocente")