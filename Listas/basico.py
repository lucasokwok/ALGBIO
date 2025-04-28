# PRIMEIROS COMANDOS EM PYTHON

# Toda variável em Python 3 é um objeto

# Variáveis primitivas
nome = 'thiago'          # string
idade = 39               # inteiro
altura = 1.75            # float
maior_de_idade = True    # booleano

# Comando print - imprime informações
print('O meu nome é Thiago')  # texto simples
print(nome)                   # imprime o valor da variável
print('A idade do Thiago é 39')  # texto fixo

# Usando format e f-string
print('A idade do Thiago é {}'.format(idade))  # forma antiga
print(f'A idade do Thiago é {idade}')          # f-string moderna

# Formatação de número com f-string
pi = 3.14159265
print(f'O valor de pi é {pi:.2f}')  # mostra com duas casas decimais

# Comando input (tudo vira string!)
entrada = input('Digite seu nome: ')
print(f'Olá, {entrada}!')

# Convertendo input para int e float
idade_digitada = int(input('Digite sua idade: '))
altura_digitada = float(input('Digite sua altura: '))

print(f'Sua idade é {idade_digitada} e sua altura é {altura_digitada:.2f}m')

# Operadores aritméticos
a = 10
b = 3
print(f'Soma: {a + b}')
print(f'Subtração: {a - b}')
print(f'Multiplicação: {a * b}')
print(f'Divisão: {a / b}')
print(f'Potência: {a ** b}')
print(f'Divisão inteira: {a // b}')
print(f'Resto da divisão: {a % b}')

# Precedência de operadores
resultado = (a + b) * 2 ** 2 / 4
print(f'Resultado com precedência: {resultado}')

# Trabalhando com strings

nome = 'thiago'

# Acessando caracteres da string
print(f'Primeira letra do nome: {nome[0]}')
print(f'Segunda letra do nome: {nome[1]}')

# Mostrando índices com laço for
for i in range(len(nome)):
    print(f'Caractere na posição {i}: {nome[i]}')

# Slicing (fatiamento) de strings
print(f'nome[0:2] = {nome[0:2]}')       # 'th'
print(f'nome[:2] = {nome[:2]}')         # 'th'
print(f'nome[-1] = {nome[-1]}')         # 'o'
print(f'nome[0:2:-1] = {nome[0:2:-1]}') # ''
print(f'nome[::-1] = {nome[::-1]}')     # 'ogaiht' (inverte a string)
print(f'nome[0:-1:2] = {nome[0:-1:2]}') # 't i g'

# Alterando partes da string (criando nova string)
novo_nome = 'TI' + nome[2:]             # substituindo os 2 primeiros caracteres
print(f'novo_nome = {novo_nome}')       # 'TIiago'

nome_modificado = nome[:-1] + '0'       # trocando último caractere
print(f'nome com último caractere trocado: {nome_modificado}')  # 'thiag0'

# Comandos úteis para string

# len() → tamanho da string
tamanho = len(nome)
print(f'Tamanho da string "{nome}" é {tamanho}')

# f-strings dentro de string
frase = 'A idade do Thiago é 39'
print(frase)
frase = f'A idade do Thiago é {idade}'
print(frase)

# MÉTODOS DE STRING (toda variável é um objeto, e pode usar métodos)

print(f"Quantidade de letras 'a' em {nome}: {nome.count('a')}")
print(f"Posição da primeira letra 'a' em {nome}: {nome.find('a')}")
print(f"Substituindo 'a' por 'x': {nome.replace('a', 'x')}")
print(f"Tudo maiúsculo: {nome.upper()}")
print(f"Tudo minúsculo: {nome.lower()}")
print(f"Primeira letra maiúscula: {nome.capitalize()}")
print(f"Nome dividido em lista: {nome.split()}")
