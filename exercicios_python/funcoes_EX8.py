# Exercicio 8
# Faça uma função que receba parâmetros variáveis. Faça algumas chamadas dessa função passando valores inteiros e, de acordo com a quantidade de parâmetros recebidos, calcule a média.


def soma_media(*num):
  soma = 0
  for i in num:
    soma += i
  return soma, (soma / len(num))

soma = soma_media(2, 8, 6, 8, 9)[0]
media = soma_media(2, 8, 6, 8, 9)[1]

print(f"Soma: {soma} e Média: {media}")