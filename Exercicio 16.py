# 16) Crie um programa que calcule a área de um quadrado ou a área de um triângulo de acordo
com a opção do usuário. Crie um menu com as seguintes opções:
1 - Área do quadrado
2 - Área do triângulo
3 – Sair
A área do quadrado é : área = lado * lado. A do triângulo é área = (base * altura)/2 . O
programa deve terminar somente quando o usuário informar a opção 3.#

  


menu = 0
while menu != 3:
    
    print('\nEscolha uma opção no menu')
    menu = int(input(('''
    [ 1 ]  Área do quadrado 
    [ 2 ] Área do triangulo
    [ 3 ] Sair ''')))
    
    
    if menu == 2:
        altura = int(input('Digite a altura do triangulo: '))

        base = int(input('Digite a base do triangulo: '))
        
        area = (base * altura)/2

        print('\nA área do triangulo é:', area)
    if menu == 1:
        lado = float(input('Digite a altura do quadrado: '))
        
        area = (lado*lado)

        print('\nA área do quadrado é de ', area) 
    
    elif menu == 3:
        print('\nPrograma finalizado')
    else:
        print('\nOpção invalida')
print('\nFim do programa')






