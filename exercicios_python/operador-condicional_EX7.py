#Exercicio 7
### Faça um programa que receba via input de usuário os valores de duas notas de uma aluna. O programa deve calcular a média alcançada e apresentar:
##### A mensagem "Aprovada", se a média alcançada for maior ou ia=gual a 7;
##### A mensagem "Reprovada", se a média for menor que 7;
##### A mensagem "Aprovada com Distinção", se a média for igual a 10


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
  if media == 10:
    print("Aprovada com distinção!")
  else:
    print("Aprovada!")
else:
  print("Reprovada!")