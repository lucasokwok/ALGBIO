# ## VARIÁVEIS SIMPLES (PRIMITIVAS)

# String (texto)
nome = str("Thiago")
print("String:", nome)

# Inteiros (números sem decimal)
idade = int(38)
print("Inteiro:", idade)

# Reais (números com decimal)
altura = float(1.78)
print("Float:", altura)

# Booleanos (Verdadeiro ou Falso)
ativo = bool(True)
print("Booleano:", ativo)

print("-" * 40)

# ## VARIÁVEIS COMPOSTAS

# ### TUPLAS → ()
# Tuplas são imutáveis (não podem ser alteradas depois de criadas)

# Tupla vazia
tupla_vazia = ()
print("Tupla vazia:", tupla_vazia)

# Tupla com elementos
a = ('thiago', 'martini', 38, 1.78)
print("Tupla completa:", a)
print("Primeiro elemento da tupla:", a[0])
print("Fatiamento da tupla:", a[0:2])

# Desempacotando tupla
w = ('thiago', 38, 1.78)
nome, idade, altura = w
print(f"Desempacotado: nome={nome}, idade={idade}, altura={altura}")

print("-" * 40)

# ### LISTAS → []
# Listas são mutáveis e ordenadas

# Lista vazia
l = []
print("Lista vazia:", l)

# Lista com elementos
l = ['thiago', 38, 2.78]
print("Lista inicial:", l)

# Modificando elementos
l[2] = 1.78
l[1] = ['martini', 'pereira']
print("Lista modificada:", l)
print("Subelemento da lista:", l[1][0])  # imprime 'martini'

# Acessando elementos
l2 = ['thiago', 'maria', 'jose', 'alberto']
print("Primeiro nome:", l2[0])
print("Primeiros dois nomes:", l2[0:2])
print("Saltando um:", l2[::2])
print("Ordem reversa:", l2[::-1])

# Cópia x Ponteiro
a = l2
a[0] = 'joão'
print("Lista original (referência):", l2)
print("Lista modificada (referência):", a)

# Cópia real
a = l2[:]
a[0] = 'thiago'
print("Lista original após cópia:", l2)
print("Cópia modificada:", a)

print("-" * 40)

# ### MÉTODOS DE LISTAS

frutas = ['maçã', 'banana', 'maçã']

# .append() → adiciona no final
frutas.append('laranja')
print("Append:", frutas)

# .count(X) → conta quantas vezes X aparece
print("Count 'maçã':", frutas.count('maçã'))

# .insert(posição, elemento)
frutas.insert(1, 'uva')
print("Insert na posição 1:", frutas)

# .pop(posição) → remove o da posição
frutas.pop(2)
print("Pop na posição 2:", frutas)

# .remove(valor) → remove o conteúdo específico
frutas.remove('banana')
print("Remove 'banana':", frutas)
