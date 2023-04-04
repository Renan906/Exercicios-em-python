# 12) Faça um script Python para conversão de segundos. O usuário irá informar os segundos
como um número inteiro. O script deve calcular quantas horas:minutos:segundos a
quantidade total de segundos digitados pelo usuário corresponde.#





segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))


segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")