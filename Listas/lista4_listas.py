# Lista 04 – listas

# 1) Leia uma lista de 10 números reais e mostre-os na ordem inversa.
lista1 = [1.5, 2.3, 4.1, 7.0, 0.5, -3.2, 9.8, 6.6, -1.1, 8.4]
print(lista1[::-1])

# 2) Leia duas listas e gere uma terceira com os elementos das duas primeiras.
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# 3) Temperaturas de Mons: imprima a menor, a maior e a média.
T = [-10, -8, 0, 1, 2, 5, -2, -4]
print(min(T))
print(max(T))
print(sum(T) / len(T))

# 4) Leia 20 números inteiros. Separe em pares e ímpares. Imprima os três vetores.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(numeros)
print(pares)
print(impares)

# 5) Peça as quatro notas de 5 alunos, calcule e armazene a média, conte quantos tiveram média ≥ 7.0
notas = [
    [7, 8, 9, 10],
    [5, 5, 6, 6],
    [10, 10, 10, 10],
    [6, 7, 6, 8],
    [2, 3, 4, 5]
]
medias = []
for aluno in notas:
    medias.append(sum(aluno) / len(aluno))
aprovados = sum(1 for m in medias if m >= 7.0)
print(aprovados)

# 6) Rotina que retorna a soma dos quadrados dos números.
def soma_quadrados(lista):
    return sum(x**2 for x in lista)

print(soma_quadrados([1, 2, 3, 4]))

# 7) Rotina que retorna somente os números ímpares usando list comprehension.
def filtrar_impares(lista):
    return [x for x in lista if x % 2 != 0]

print(filtrar_impares([1, 2, 3, 4, 5, 6, 7]))

# 8) Função que retorna a string mais longa de uma lista.
def string_mais_longa(lista):
    return max(lista, key=len)

print(string_mais_longa(["atgc", "gattaca", "ac", "tgaaa"]))
