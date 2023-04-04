#Faça um script Python para ler 3 números reais e exibir a soma do 1º número com o 2º
multiplicada pela soma do 2º com o 3º.#



n1 = float(input('Digite o primeiro valor : '))
n2 = float(input('Digite o segundo valor : '))
n3 = float(input('Digite o terceiro valor : '))

s = (n1+n2)*(n2+n3)

print(f'O resultado é {s} .')