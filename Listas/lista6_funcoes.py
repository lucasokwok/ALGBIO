# 1) Escreva uma função chamada fatorial para calcular o
# fatorial de um número inteiro.
#5! = 5.4.3.2.1
def fatorial(n : int):
    result = 1
    if n == 0:  
        return 1
    for i in range(1, n + 1):
        result = result * i
    return result

# n = int(input())
# print(f'{fatorial(n)}')

# 2) Escreva uma função chamada maxnum que retorne o maior
# número de um conjunto de números. Utilize
# empacotamento para fazer a função.
def maxnum(*n):
    result = n[0]
    for numero in n:
        if numero > result:
            result = numero

    return result

# print(f'{maxnum(1,4,5,6,9,2)}')

# 3) Escreva uma função que receba dois números e retorne
# True se o primeiro número for múltiplo do segundo.
def mult(x : int, y : int):
    return(x % y == 0)

# print (f'{mult(5,10)}')
# 4) Crie uma função chamada "calculadora" que recebe três
# parâmetros: dois números e uma operação matemática (+,
# -, *, /). A função deve retornar o resultado da operação.
def calculadora(x : int, y: int, op):
    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        
# print(f'{calculadora(10,10,'/')}')
# 5) Crie uma função chamada "maior_palavra" que recebe
# uma lista de palavras como parâmetro e retorna a maior
# palavra dessa lista.
def maior_palavra(palavras : list):
    lenmaiorpalavra = len(palavras[0])
    maiorpalavra_index = 0

    for i in range(1, len(palavras)):
        if len(palavras[i]) > lenmaiorpalavra:
            maiorpalavra_index = i
            lenmaiorpalavra = len(palavras[i])

    return palavras[maiorpalavra_index]

# entrada = input("Digite várias palavras separadas por espaço: ")
# lista_palavras = entrada.split()
# print(f"A maior palavra é: {maior_palavra(lista_palavras)}")

# 6) Implemente uma função chamada "soma_recursiva" que
# recebe um número inteiro positivo como parâmetro e
# retorna a soma de todos os números inteiros de 1 até esse
# número, utilizando recursividade.
import math

def soma_recursiva(n : int):    
    if n == 1: 
        return 1
    return n + soma_recursiva(n-1)

# print(f'{soma_recursiva(5)}')

# 7) Crie uma função na qual calcula o valor do seno a partir da
# série de Taylor (50 primeiros termos) e cosseno a partir da
# seguinte identidade a baixo. Obs: Fazer a serie utilizando for
# e utilizar a função fatorial desenvolvida no exercício 1.

# cos (x)

# 2 + sen(x)

# 2 = 1

def cosseno(x : float):
    senx = 0
    sinal = 0 # 0 = +; 1 = -
    for i in range(1, 100, 2):
        if sinal == 0:
            senx += pow(x, i)/fatorial(i)
            sinal = 1
        else:
            senx -= pow(x, i)/fatorial(i)
            sinal = 0

    return math.sqrt(1 - pow(senx, 2))

#melhoria: enumerate devolve um par (indice, numero), no caso o for executa 50 vezes (indices 0 - 49) e o numero que é a variavel i
# será os numeros ímpares entre 1 e 100
for k, i in enumerate(range(1, 100, 2)):
    termo = ((-1) ** k) * (x**i / fatorial(i))
    senx += termo


    
