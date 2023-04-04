# 19) Crie um script Python que informe ao usuário quando deve ser pago o IPVA de seu carro,
baseado no último digito da placa. Peça para o usuário entrar simplesmente com o último
dígito da placa. Veículos com placa de final 1, Imposto em Janeiro; final 2 Fevereiro; final 3
Março e todo o restante deve pagar o IPVA(imposto) em Abril. #



n1 = int(input('\nEntre com o ultimo digito da sua placa: '))



if (n1==1):
  print('\nPagar o IPVA(Imposto) em Janeiro ')

elif (n1==2):
  print('\nPagar o IPVA (Imposto) em Fevereiro ')
  
elif (n1==3):
  print('\nPagar o IPVA (Imposto) em Março ')

else:
  print('\nPagar o IPVA (imposto) em Abril. ')

