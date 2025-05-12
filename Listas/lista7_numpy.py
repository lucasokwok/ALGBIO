import numpy as np

# 1. Crie um array contendo os números inteiros de 10 a 19 utilizando np.arange.
np.arange(10, 20, 1) # np.arange(início, fim, passo)

# 2. Crie uma matriz 3x4 preenchida com zeros do tipo float.
matriz = np.zeros((3, 4), dtype=float)

# 3. Crie um array contendo 15 valores igualmente espaçados entre 0 e 5, incluindo
# os extremos, usando np.linspace.
valores = np.linspace(0, 5, 15)

# 4. Crie um array com valores inteiros e converta-o para o tipo float64 utilizando o
# método .astype().
inteiros = np.array([1, 2, 3, 4, 5])
floats = inteiros.astype(np.float64)

# 5. Dado o array a = np.array([[10, 20, 30], [40, 50, 60]]), acesse: 
# (a) o elemento da 2a linha e 3a coluna, 
# (b) a primeira linha inteira, e 
# (c) todos os elementos da coluna 2.
a = np.array([[10, 20, 30], [40, 50, 60]])
elemento = a[1][2]
linha = a[0]
coluna2 = a[:, 1]

# 6. Dado x = np.array([1, 2, 3]) e y = np.array([4, 5, 6]), realize: 
# (a) a soma elemento a elemento, 
# (b) a multiplicação elemento a elemento, e 
# (c) a subtração y - x.
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

soma = x + y
produto = x * y
subtracao = y - x

# 7. Dado um array z = np.array([2, 4, 6, 8]), subtraia 1 de todos os elementos e
# multiplique o resultado por 2.
z = np.array([2, 4, 6, 8])
z -= 1
z *= 2

# 8. Crie duas matrizes 2x2 com valores à sua escolha e calcule o produto matricial
# entre elas usando a função np.dot(). que é a multiplicação de matrizes linhaxcoluna

# Matrizes 2x2 com valores escolhidos
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

p = np.dot(A, B)

# 9. Utilize a função np.exp para calcular e^x para os valores de x = [0, 1, 2, 3, 4].
x = np.array([0, 1, 2, 3, 4])
result = np.exp(x)

# 10. Implemente uma função que calcule a soma dos 20 primeiros termos da seguinte
# série de Taylor.

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def seno_taylor(x):
    soma = 0
    for n in range(20):  
        numerador = (-1)**n * x**(2*n + 1)
        denominador = fatorial(2*n + 1)
        termo = numerador / denominador
        soma += termo
    return soma

# 11. Crie uma matriz identidade de tamanho 5x5 usando np.eye.
identidade = np.eye(5)

# 12. Gere uma matriz 4x4 com números aleatórios de ponto flutuante entre 0 e 1
# utilizando np.random.rand.
matriz = np.random.rand(4, 4)

# Dado o array a = np.array([2, 4, 6, 8, 10]), calcule a média, o desvio padrão e a
# soma total dos elementos utilizando funções do NumPy.
a = np.array([2, 4, 6, 8, 10])
media = np.mean(a)
desviopadrap = np.std(a)
soma = np.sum(a)

# 13. Crie um array 1D com 12 elementos e transforme-o em uma matriz 3x4 usando
# .reshape.
a = np.arange(1, 13, 1)
b = a.reshape(3, 4)

# 14. Crie dois arrays 1D de 5 elementos e use np.concatenate para juntá-los em um
# único array 1D.
a = np.arange(1, 6, 1)
b = np.arange(6, 11, 1)

c = np.concatenate(a, b)