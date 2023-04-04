# 14) Escreva um script Python que calcule, a partir de dois dados fornecidos pelo usuário, o
valor de x + a, onde “a” é uma porcentagem do valor de x, que deve ser acrescentada a x.#



x = float(input('Digite um número: '))
a = float(input('Digite outro número: '))

p = a/100 * x 

calculo = x + p


print(f'O valor é {calculo}')