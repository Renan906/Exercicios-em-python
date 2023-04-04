#Criem um programa que calcule o valor de delta, usando a fórmula delta = b^2 - 4ac.
Peça os valores para o usuário. Use variáveis do tipo real (float).#



a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2-4*a*c

print(f'delta é igual a: {delta}.')

