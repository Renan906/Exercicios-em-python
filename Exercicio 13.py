# 13) Escreva um script Python que calcule o termo n de uma Progressão Aritmética (PA). O
programa deve receber como entrada do usuário o primeiro termo da PA (a0), o segundo
termo (a1) e o valor de N. Uma PA é qualquer sequência na qual cada termo, a partir do
segundo, é obtido somando-se ao anterior uma certa constante denominada razão da
progressão aritmética. Descubra qual é a razão para calcular os “n” termos. Exemplo:
Entrada: a0 = 4;
 a1 = 19;
 n = 6;
Saída: a6 = 94
Pois, o termo inicial (a0) e os seis (n) termos serão: 4 ; 19 ; 34 ; 49; 65 ; 79 ; 94.
#







primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
n = int(input("Quantos elementos exibir: ") )

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for var in range(primeiro, ultimo, razao):
    print(var)

