# 17) Crie um script Python que informe a quantidade de DÍGITOS que são números PARES, dado
um número inteiro digitado pelo usuário. Exemplo: Número 27638, quantidade de dígitos
pares é 3, ou seja, somente os dígitos 2, 6 e 8 são pares. Utilize o operador resto (%) para
obter os dígitos separados, e.g., número 1234 quando dividido por 10 utilizando o operador
resto é igual a 4. Se repetir o mesmo procedimento para 123 o resto é 3 (use a divisão por 10
para conseguir o 123 a partir de 1234). Utilize uma repetição na solução. O resto da divisão por
2 de um número “par” é zero, i.e., 10%2 no Python será zero, pois 10 é par.#

a = input('Digite um número: ')
par = 0

for i in range (len(a)):
  numero = int(a[i]) % 2
  if numero == 0:
    par += 1
    continue
  else:
    continue
print (par)

