# Lista 03 – loops e condicionais

# 1) Duas funções que recebem um pH e exibem o tipo de solução.
def tipo_solucao_if(ph):
    if ph < 7:
        print("A solução é ácida")
    elif ph > 7:
        print("A solução é básica")
    else:
        print("A solução é neutra")

def tipo_solucao_ternaria(ph):
    print("A solução é " + ("ácida" if ph < 7 else "básica" if ph > 7 else "neutra"))

tipo_solucao_if(6.5)
tipo_solucao_ternaria(7)

# 2) Script que analisa resposta 's', 'n' ou outra.
resposta = 'S'
if resposta in ['s', 'S']:
    print("OK, continuando...")
elif resposta in ['n', 'N']:
    print("OK, parando...")
else:
    print("Resposta inválida.")

# 3) Contagem regressiva do lançamento.
for i in range(10, -1, -1):
    print(i)
print("Fogo!")

# 4) Sequência de Fibonacci até o décimo termo.
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b

# 5) Números primos entre 1 e 100.
for num in range(2, 101):
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)

# 6) Determinar se um número é primo.
n = 29
if n < 2:
    print("Não é primo")
else:
    primo = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primo = False
            break
    print("É primo" if primo else "Não é primo")

# 7) Simulador de caixa eletrônico.
valor = 376
notas = [100, 50, 20, 10, 5, 2]
for nota in notas:
    qtd = valor // nota
    valor %= nota
    print(f"{qtd} nota(s) de R${nota}")

# 8) Cálculo do IMC com classificação.
peso = 70
altura = 1.75
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"
print(f"IMC = {imc:.2f} -> {classificacao}")

# 9) Verificar número de Armstrong.
num = 153
digitos = [int(d) for d in str(num)]
soma = sum(d**len(digitos) for d in digitos)
print("É de Armstrong" if soma == num else "Não é de Armstrong")

# 10) Aproximação da constante e com erro < α.
alpha = 1e-8
from math import factorial
e_aprox = 0
n = 0
while True:
    termo = 1 / factorial(n)
    e_aprox += termo
    if termo < alpha:
        break
    n += 1
print(f"Constante e ≈ {e_aprox:.8f}")
print(f"n = {n}")
