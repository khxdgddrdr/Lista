pa = input("Digite uma palavra: ")
n_palavra = ""

for caractere in pa:
    novo_valor_ascii = ord(caractere) + 1
    novo_caractere = chr(novo_valor_ascii)
    n_palavra += novo_caractere

print("A nova palavra é:", n_palavra)
