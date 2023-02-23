# Exercicio 5
# Usar um loop for que faça a tabuada do 2. A saída esperada é 

##### 2 x 0 = 0
##### 2 x 0 = 1
##### 2 x 2 = 4
##### ...
##### 2 x 9 = 18



num_tabuada = 2
tabuada = 0

while tabuada <= 10:
  print(f'{num_tabuada} x {tabuada} = {num_tabuada * tabuada}')
  tabuada +=1