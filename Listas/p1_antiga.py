#1. IMC abaixo de 24,9 = Peso normal
# Entre 25 e 29,9 = Sobrepeso
# Maior que 30 = Obesidade
# n = int(input("Quantidade de pessoas:"))

# pessoas = []
# for i in range(n):
#     nome = input("Nome:")
#     sexo = input("Sexo:")
#     peso = float(input("Peso em kg:"))
#     altura = float(input("Altura em m:"))
#     imc = peso / pow(altura, 2)

#     if imc <= 24.9:
#         situacao = "Peso normal"
#     elif 25 <= imc <= 29.9: 
#         situacao = "Sobrepeso"
#     else:
#         situacao = "Obesidade"

#     pessoa = {
#         "nome" : nome,
#         "sexo" : sexo,
#         "peso" : peso,
#         "altura" : altura,
#         "imc" : f'{imc:.4f}', # com 4 casas decimais
#         "situacao" : situacao
#     }

#     pessoas.append(pessoa)

# print(pessoas)

#2. 
#a) crie uma funcao que ordene um vetor de números em ordem crescente

def bubble_sort(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor) - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor

vetor = [7,9,5,2,3,6,1,4,0]
# print(bubble_sort(vetor))

#b) 
def media_unifesp(nome : str, ra : int, mediaF : float):
    return {
        "nome" : nome,
        "ra" : ra,
        "mediaF" : mediaF,
        "situacaoF" : "Aprovado" if mediaF >= 6 else "Reprovado"
    }

# print(media_unifesp("Lucas", 163919, 7))

#3.
#a) funcao para imprimir os numeros primos de 1 a 100
def primos():
    for i in range(2, 101): # começa no 2 pq 1 nao é primo
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)
# primos()

#b) funcao que calcule o fatorial
# def fatorial(n:int): PORÉM e exercício pede para utilizar FOR
#     if n == 0 : return 1
#     return n * fatorial (n-1)

# print(fatorial(5))

def fatorial(n:int):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# print(fatorial(0))

#4. 
import numpy as np

def cossenhiper(rad:float):
    cosh = 0
    for i in range(20):
        cosh += (1/(fatorial(2*i)))*(pow(rad, (2*i)))
    # senh^2 = cosh^2 -1
    senh = pow((pow(cosh,2) - 1),1/2)
    return cosh, senh

print(cossenhiper(0))