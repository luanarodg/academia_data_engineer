# Exercicio 5
### Criar uma função chamada "imprime_tabuada. Usando o for, imprimir as tabuadas de 1 a 9, no mesmo formato do exercício anterior:

##### 2 x 0 = 0
##### 2 x 1 = 2
##### ...
##### 2 x 10 = 20


def imprime_tabuada():
  for i in range(2, 10):
    print(f"\nTabuada do {i}")
    for j in range(11):
      print(f"{i} x {j} = {i * j}")


imprime_tabuada()