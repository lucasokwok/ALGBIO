# Lista 02 – strings

# 1. Crie duas variáveis contendo trechos de DNA e concatene-as para formar uma sequência maior.
s1 = "ATGC"
s2 = "TGA"
print(s1 + s2)

# 2. Se uma sequência contém "AG", use um operador para repeti-la cinco vezes.
seq = "AG"
print(seq * 5)

# 3. Use a função len() para descobrir quantos nucleotídeos há na sequência "ATGCGTAC".
print(len("ATGCGTAC"))

# 4. Dada a string "AGCTGA", imprima a primeira e a última base nitrogenada.
s = "AGCTGA"
print(s[0], s[-1])

# 5. Dada a sequência "CGTACGTAGC", exiba apenas os cinco primeiros nucleotídeos.
print("CGTACGTAGC"[:5])

# 6. Pegue a sequência "TACGATCGG" e exiba apenas os três últimos nucleotídeos.
print("TACGATCGG"[-3:])

# 7. A partir da sequência "AATGCGTACG", exiba apenas os quatro nucleotídeos centrais.
s = "AATGCGTACG"
print(s[3:7])

# 8. Converta "atgcgtac" para maiúsculas e "ACGTGCA" para minúsculas.
print("atgcgtac".upper())
print("ACGTGCA".lower())

# 9. Substitua todas as ocorrências da base "A" pela base "T" na sequência "AAGCTA".
print("AAGCTA".replace("A", "T"))

# 10. A sequência "  ATG CCA GTC  " contém espaços extras. Remova-os e imprima o resultado.
print("  ATG CCA GTC  ".replace(" ", ""))

# 11. Defina três variáveis com segmentos genéticos e una-os para formar um gene completo.
a = "ATG"
b = "GCA"
c = "TGA"
print(a + b + c)

# 12. Verifique se a sequência "TATA" está contida na string "ATGCTATAAGC" e exiba o resultado.
print("TATA" in "ATGCTATAAGC")

# 13. Conte quantas vezes a base "G" aparece na sequência "GGTACGGGCA".
print("GGTACGGGCA".count("G"))

# 14. Use f-strings para exibir a mensagem "O gene X tem Y nucleotídeos", substituindo X e Y por valores de variáveis.
gene = "ATGCGTAC"
print(f"O gene {gene} tem {len(gene)} nucleotídeos")

# 15. Inverta a string "ATGCGTA" utilizando fatiamento para simular a fita complementar.
print("ATGCGTA"[::-1])
