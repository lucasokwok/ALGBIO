import random

def criptografia(frase : str, k : int):
    novaFrase = ""
    for caracter in frase:
        
        if caracter.isalpha():
            if 'A' <= caracter <= 'Z':  
                caracter.lower()

            asc = ord(caracter)
            caracter = chr(asc + k)

        novaFrase += caracter
    print(novaFrase)

frase_original = input("Mensagem de entrada")
k = random.randint(1 ,25)
print(f"Mensagem criptografada com k={k}")
criptografia(frase_original, k)