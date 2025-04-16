# Lista 05 – dicionários

# 1) Gere um dicionário onde cada chave seja um caractere e o valor seja o número de vezes que ele aparece em uma frase.
frase = "O rato"
dicionario = {}
for letra in frase.replace(" ", ""):
    dicionario[letra] = dicionario.get(letra, 0) + 1
print(dicionario)

# 2a) Crie um dicionário de frutas e seus preços.
frutas = {"banana": 3.5, "maçã": 4.0, "abacaxi": 6.5, "uva": 2.8}

# 2b) Crie um dicionário de compras e calcule o valor total.
compras = {"banana": 2, "maçã": 3, "abacaxi": 1}
total = sum(frutas[fruta] * quantidade for fruta, quantidade in compras.items())
print(total)

# 2c) Remova todas as frutas que custam mais de R$ 5,00.
frutas = {fruta: preco for fruta, preco in frutas.items() if preco <= 5.0}
print(frutas)

# 3) Leia nome, RA e média final, defina a situação (UNIFESP).
aluno = {"nome": "Ana", "RA": "123456", "media": 6.0}
if aluno["media"] < 4:
    aluno["situacao"] = "Reprovado"
elif aluno["media"] < 7:
    aluno["situacao"] = "Exame"
else:
    aluno["situacao"] = "Aprovado"
print(aluno)

# 4) Leia nome, sexo, peso e altura de várias pessoas. Calcule o IMC, salve em lista e mostre médias.
pessoas = [
    {"nome": "João", "sexo": "M", "peso": 70, "altura": 1.75},
    {"nome": "Maria", "sexo": "F", "peso": 60, "altura": 1.65},
    {"nome": "Carlos", "sexo": "M", "peso": 80, "altura": 1.80}
]

for p in pessoas:
    p["imc"] = p["peso"] / (p["altura"] ** 2)

qtd = len(pessoas)
peso_medio = sum(p["peso"] for p in pessoas) / qtd
altura_medio = sum(p["altura"] for p in pessoas) / qtd
imc_medio = sum(p["imc"] for p in pessoas) / qtd

print(qtd)
print(round(peso_medio, 2))
print(round(altura_medio, 2))
print(round(imc_medio, 2))

# 5) Agrupar uma lista de dicionários por uma chave específica.
lista = [
    {"nome": "Ana", "curso": "Bio"},
    {"nome": "João", "curso": "Comp"},
    {"nome": "Carlos", "curso": "Bio"}
]
agrupado = {}
for item in lista:
    chave = item["curso"]
    agrupado.setdefault(chave, []).append(item)
print(agrupado)

# 6) Criar um set de todos os caracteres únicos em uma string.
texto = "biocomputação"
caracteres_unicos = set(texto)
print(caracteres_unicos)

# 6) Gerenciar o aproveitamento de um jogador.
jogador = {"nome": "Pedro", "gols": []}
partidas = 3
gols_partidas = [1, 0, 2]
jogador["gols"] = gols_partidas
jogador["total"] = sum(gols_partidas)
print(jogador)

# 7) Verificar se uma chave específica existe no dicionário.
d = {"a": 1, "b": 2}
chave = "b"
print(chave in d)
