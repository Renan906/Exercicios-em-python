#Escreva um script Python ler dois inteiros e exibir o resto da divisão do primeiro pelo
segundo. Se o usuário quiser dividir um número por zero, faça a verificação de divisão por zero
e informe que não é possível esta operação.#




n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

resto = n1 % n2



if (n1 and n2 > 0):

  print(f'O resto da divisão é {resto}')

else:

  print(f'Não é possivel fazer essa operação ')