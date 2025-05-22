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
#         situacao = "Obesidade" #faltou a situação exame que é média final >= 3

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

# print(cossenhiper(0))

# OUTRA p1 antiga
#2. 
#a) funcao para remover todos os elementos duplicados de uma lista
def remover_duplicados(lista):
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado


vetor = [1,1,1,1,1,2,2,2,2]
vetor = remover_duplicados(vetor)

# print(vetor)

#b)
import numpy as np
def maiormenor(lst : list):
    maior = lst[0]
    menor = lst[0]

    for i in range(len(lst)):
        if maior < lst[i]:
            maior = lst[i]
        if menor > lst[i]:
            menor = lst[i]
    return maior, menor

def maiormenornp(lst : list):
    a = np.array([lst])
    return int(a.max()), int(a.min())

# print(maiormenor([1,2,3,4,1,2,3,12,3,46,7, 0, -7]))
# print(maiormenornp([1,2,3,4,1,2,3,12,3,46,7, -2]))

#3. 
def soma_digitos():
    numero = input("Digite um número inteiro: ")
    soma = 0
    for digito in numero:
        soma += int(digito)    
    print(f"Soma dos dígitos: {soma}")

dados = {
    "nome": "Lucas",
    "idade": 21,
    "curso": "Engenharia",
    "ativo": True
}

for chave, valor in dados.items():
    print(f"{chave} → {valor}")

def quadrados_pares(lista):
    return [x ** 2 for x in lista if x % 2 == 0]

entrada = [1, 2, 3, 4, 5, 6]
saida = quadrados_pares(entrada)
print(saida)  # Saída: [4, 16, 36]

#p ajudar a entender list comprehension
#Aqui está uma função simples que usa list comprehension para filtrar apenas os números pares de uma lista:

def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(numeros)
print(pares)  # Saída: [2, 4, 6, 8, 10]


