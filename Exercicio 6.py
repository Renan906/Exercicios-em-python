# Considere que uma pessoa investe inicialmente R$1 500,00 em uma conta poupança
rendendo 8% de juros ao ano. Se esta pessoa não retirar nenhum valor da conta e ainda
adiciona mais R$ 557,00 a cada ano, quanto em R$ haverá nesta conta ao fim de 25 anos? Faça
um script Python que mostre este resultado, pedindo para o usuário digitar o valor de
investimento inicial e anual.#




invinicial = float(input('Insira o valor de  investimento inicial : '))
invanual = float(input('Insira o valor de investimento anual: '))


acumulado = float(invinicial)
i = 0

while i < 24:

  acumulado = acumulado*1.08
  acumulado += invanual

  i = i+1

print('Capital final: ',acumulado)

