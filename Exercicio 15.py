# 15) A Copa do Mundo de Futebol é realizada de 4 em 4 anos. No ano de 2014 foi disputada a
20ª Copa do Mundo. Escreva um script Python que receba do usuário um número n maior ou
igual a 20, e exiba em que ano será realizada a n-ésima Copa do Mundo#

a = 2014
r = 4

n1 = int(input('Qual copa você quer saber que ano vai acontecer? '))

if n1 >= 20:
  a1 =  a +(r *(n1 - 20))
  print(f"A {n1} Copa do Mundo ocorrerá no ano de {a1}. ")

else:
  print("Apenas valores iguais ou maiores que 20 são validos. ")




