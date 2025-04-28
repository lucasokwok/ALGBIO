# belamatematica.py

def bela_matematica():
    numero = ""
    for i in range(1, 9):
        numero += str(i)
        resultado = int(numero) * 8 + i
        print(f"{numero} x 8 + {i} = {resultado}")

if __name__ == "__main__":
    print("bela matematica")
    bela_matematica()
