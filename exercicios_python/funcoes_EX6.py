# Exercicio 6
# Faça uma função que receba 4 notas em valor decimal, entre 0 e 10. Caso a nota seja menor que 5, retornar "Reprovada". Caso a nota esteja entre 5 e 7, retornar "Está na média". Caso a nota esteja maior que 7, retornar "Aprovada".


def notas(nota1, nota2, nota3, nota4):
  media = (nota1 + nota2 + nota3 + nota4) / 4
  if media < 5:
    return "Reprovada"
  elif 5 <= media < 7:
    return "Está na média"
  return "Aprovada"

notas(7, 7, 7, 7)