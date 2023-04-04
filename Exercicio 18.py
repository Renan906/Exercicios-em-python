# 18) Faça um script Python para entrar com uma distância em (Km), o tempo de viagem em
horas e dizer se a velocidade média foi superior ao limite de 80 Km/h ou não. #



n1 = int(input('\nDigite a distancia (Km): '))
n2 = int(input('\nDigite o tempo de viagem (horas): '))

Vmedia = n1/n2



if (Vmedia > 80):

  print('\nVelocidade media foi superior a 80km/h')

else:

  print('\nVelocidade media inferior a 80km/h  ')

