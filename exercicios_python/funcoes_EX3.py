# Exercicio 3
# Faça uma função que receba um argumento inteiro. A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo

def positivo_negativo(n):
  if n <= 0:
    return ("N")
  return("P")

positivo_negativo(8)