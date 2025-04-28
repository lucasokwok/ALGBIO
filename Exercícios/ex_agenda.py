n = int(input("qtd de pessoas:"))

agenda = []
for _ in range(n):
    nome = input("Digite o nome:")
    tel = input("Digite o telefone:")
    cpf = input("Digite o CPF:")
    endereco = input("Digite o endereço:")

    contato = {
        "nome" : nome,
        "telefone" : tel,
        "cpf" : cpf,
        "endereco" : endereco
    }

    agenda.append(contato)
print(agenda)