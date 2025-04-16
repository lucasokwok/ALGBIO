# Lista 01 - primeiros comandos

# 1) Crie um script em Python que solicite o nome, altura e peso de uma pessoa e mostre a seguinte mensagem: “João tem 90 kilos e altura de 1.78 e portanto o IMC é de 28.4”.
nome = "João"
peso = 90
altura = 1.78
imc = peso / (altura ** 2)
print(f"{nome} tem {peso} kilos e altura de {altura} e portanto o IMC é de {round(imc, 1)}")

# 2) Escreva um script que leia um valor em metros e o exiba convertido em milímetros
metros = 5
milimetros = metros * 1000
print(milimetros)

# 3) Escreva um script que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.
dias = 2
horas = 5
minutos = 30
segundos = 10
total_segundos = dias*86400 + horas*3600 + minutos*60 + segundos
print(total_segundos)

# 4) Faça um script que calcule o aumento de salário. Solicite o salário e a porcentagem. Exiba o valor do aumento e do novo salário.
salario = 2000
porcentagem = 10
aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento
print(aumento)
print(novo_salario)

# 5) Leia a temperatura em graus Celsius e converta para Fahrenheit.
celsius = 30
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# 6) Escreva um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa.
peso = 80
altura = 1.75
imc = peso / (altura ** 2)
print(imc)

# 7) Leia o valor de um produto e calcule o valor final com 10% de desconto.
valor = 100
desconto = valor * 0.10
valor_final = valor - desconto
print(valor_final)

# 8) Crie um programa que calcule o tempo de viagem, pedindo ao usuário a distância e a velocidade.
distancia = 300
velocidade = 100
tempo = distancia / velocidade
print(tempo)

# 9) Escreva um script que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias. Calcule o preço a pagar.
km = 500
dias = 3
preco = (dias * 60) + (km * 0.15)
print(preco)

# 10) A resistência combinada de três resistores R1, R2 e R3 em paralelo é dada por 1/R = 1/R1 + 1/R2 + 1/R3
r1 = 100
r2 = 200
r3 = 300
resistencia_resultante = 1 / (1/r1 + 1/r2 + 1/r3)
print(resistencia_resultante)
