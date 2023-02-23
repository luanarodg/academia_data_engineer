# Exercicio 6
### Usando loops, fazer um programa que demonstra a tabuada do 2 até o 9. A saída esperada é 

##### 2 x 0 = 0
##### ...
##### 2 x 9 = 18
##### ...
##### 4 x 0 = 0
##### ...
##### 4 x 9 = 36


for i in range(2, 10):
  print(f"\nTabuada do {i}")
  for j in range(11):
    print(f"{i} x {j} = {i * j}")