# Exercício 2 
# Usando estruturas de repetição, faça um programa que leia 5 números via input de usuário e exiba a soma e a média dos números

lista = []

for i in range(0, 5):
  lista.append(int(input("Digite os números: ")))

print(f"O soma dos números é {sum(lista)}")
print(f"A média dos números é {sum(lista)/len(lista)}")