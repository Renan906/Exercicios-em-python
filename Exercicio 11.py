# 11) Escreva um script Python para ler dois valores reais e exibir o primeiro com acréscimo de
30% e o segundo com desconto de 25%.#



n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

acrescimo = n1*1.30
acrescimo2 = n2*0.25


print(f'O valor {n1} com aumento de 30% é {acrescimo} \nO desconto de 25% de {n2} é {acrescimo2}')