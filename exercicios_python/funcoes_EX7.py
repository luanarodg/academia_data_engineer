# Exercicio 7
# Faça uma função que receba 5 números e imprima a soma e a média dos números

def soma_media(num1, num2, num3, num4, num5):
  soma_num = (num1 + num2 + num3 + num4 + num5) / 4

  return (f"A soma é {soma_num} e a média é {soma_num / 5}")


soma_media(1, 4, 5, 8, 6)