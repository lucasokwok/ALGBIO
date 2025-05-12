# Exemplo 1: Contando de 0 até 4 (5 não é incluído)
for i in range(5):
    print(f"Exemplo 1 - i vale: {i}")  # 0, 1, 2, 3, 4

# Exemplo 2: Contando de 1 até 5
for i in range(1, 6):
    print(f"Exemplo 2 - i vale: {i}")  # 1, 2, 3, 4, 5

# Exemplo 3: Contando de 0 até 10 pulando de 2 em 2
for i in range(0, 11, 2):
    print(f"Exemplo 3 - i vale: {i}")  # 0, 2, 4, 6, 8, 10

# Exemplo 4: Contando de trás pra frente, de 5 até 1
for i in range(5, 0, -1):
    print(f"Exemplo 4 - i vale: {i}")  # 5, 4, 3, 2, 1

# Exemplo 5: Percorrendo cada letra de uma string
for letra in "Python":
    print(f"Exemplo 5 - Letra: {letra}")  # P, y, t, h, o, n

# Exemplo 6: Percorrendo uma lista de nomes
nomes = ["Ana", "Bruno", "Carlos"]
for nome in nomes:
    print(f"Exemplo 6 - Nome: {nome}")  # Ana, Bruno, Carlos

# Exemplo 7: Usando enumerate para acessar índice e valor
for i, nome in enumerate(nomes):
    print(f"Exemplo 7 - Posição {i}, Nome: {nome}")  # índice e valor

# Exemplo 8: Percorrendo um dicionário (chaves e valores)
idades = {"Ana": 20, "Bruno": 25, "Carlos": 30}
for nome, idade in idades.items():
    print(f"Exemplo 8 - {nome} tem {idade} anos")  # chave e valor

# Exemplo 9: Aninhando dois fors (tabuada do 1 ao 3)
for i in range(1, 4):          # i = 1, 2, 3
    for j in range(1, 11):     # j = 1 a 10
        print(f"{i} x {j} = {i*j}")  # multiplicação
    print("----------")

# Exemplo 10: Lista por compreensão (list comprehension)
quadrados = [x*x for x in range(6)]  # gera lista de quadrados
print(f"Exemplo 10 - Quadrados: {quadrados}")  # [0, 1, 4, 9, 16, 25]
