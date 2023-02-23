# Exercício 1
# Usando estruturas de repetição, faça um programa que leia 5 números via input de usuário e exiba qual é o maior número

lista = []

for i in range(0, 5):
  lista.append(int(input("Digite os números: ")))

print(f"O maior número é {max(lista)}")