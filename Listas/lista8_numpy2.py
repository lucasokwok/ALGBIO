import numpy as np
# 1. Crie duas matrizes A e B de tamanho 2x2 com valores inteiros quaisquer e calcule
# as operações: soma, subtração, multiplicação elemento a elemento e produto
# matricial.
A = np.array([[1, 2],
            [3, 4]])

B = np.array([[5, 6],
            [7, 8]])

soma = A + B
subtracao = A - B
mult = A * B
prodmatricial = np.dot(A, B)

# 2. Verifique se a matriz A do exercício anterior possui inversa. Caso sim, calcule-a.
# Em seguida, calcule o determinante de A.
det_A = np.linalg.det(A)
# matriz possui inversa se determinante diferente de 0
if det_A != 0:
inversaA = np.linalg.inv(A)

# 3. Gere uma matriz 3x3 com valores inteiros e calcule sua transposta. Depois,
# multiplique a matriz por sua transposta e verifique se o resultado é simétrico.
A = np.array([[1, 2 , 3],
            [4, 5, 6],
            [7, 8, 9]])
A_t = A.transpose() # ou
A_t = A.T

# Uma matriz é simétrica se for igual à sua transposta
B = np.dot(A, A_t)

if np.array_equal(B, B.T):
    # é simétrica
    print("é simétrica")


# 4. A partir do array a = np.array([[2, 5, 3], [8, 6, 9]]), calcule o valor mínimo e
# máximo da matriz inteira, por linha e por coluna, além da soma total, média e
# desvio padrão.
a = np.array([[2, 5, 3], [8, 6, 9]])

minimo_total = a.min()
minimo_por_coluna = a.min(0)
minimo_por_linha = a.min(1)

maximo_total = a.max()
maximo_por_coluna = a.max(0)
maximo_por_linha = a.max(1)

soma = a.sum()
media = a.mean()
desviop = a.std()

# 5. Crie uma matriz de uns com forma 4x3 e, utilizando .reshape, converta-a nos
# formatos 6x2 e 12x1 e vetor 1D.
a = np.zeros((4, 3))
a.reshape(6,2)
a.reshape(12, 1)
a.reshape(12)

# 6. Crie duas matrizes de tamanho 2 x 3 e realize a concatenação horizontal e vertical
# entre elas, explicando quais condições devem ser satisfeitas para cada caso.

# 7. Gere uma matriz 3x3 com inteiros aleatórios entre 0 e 3 e replique-a duas vezes
# na vertical, na horizontal e em ambas as direções utilizando np.tile.

# 8. Crie um array 3 \times 3 com valores de 0 a 8 e gere um array booleano indicando
# onde os valores são maiores que 5. Substitua esses valores por -1 no array
# original.

# 9. Simule duas matrizes A e B com a mesma forma e preencha com inteiros entre 0
# e 10. Substitua em B os valores correspondentes onde A > 5 pelos valores de A.

# 10. Simule um array com valores de temperatura de 20 sensores biomédicos.
# Marque com True os valores fora da faixa fisiológica (menor que 36 °C ou maior
# que 38 °C).

# 11. Com a matriz m = np.arange(1, 10).reshape(3, 3), selecione as duas primeiras
# linhas e colunas a partir da segunda coluna. Em seguida, selecione a última linha
# da matriz.

# 12. Usando a matriz do exercício anterior, aplique fatiamento booleano para obter
# apenas os valores maiores que 5.

# 13. Crie um array com 100 valores igualmente espaçados entre 0 e 2pi, e calcule o
# seno, cosseno e tangente desses valores usando funções do NumPy.

# 14. Plote os gráficos das três funções trigonométricas do exercício anterior
# utilizando o matplotlib.pyplot, exibindo título, legenda e rótulos nos eixos.