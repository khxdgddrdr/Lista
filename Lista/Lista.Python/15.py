fra = "Esta é uma frase de exemplo."
con = 0

for caractere in fra:
    if caractere.isspace():
        con += 1

print("A frase tem", con, "caracteres em branco.")
