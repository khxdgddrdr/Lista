pla = input("Digite uma palavra de até 10 caracteres: ")
vos = "aeiouAEIOU"

n_vogais = 0
for letra in palavra:
    if letra in vogais:
        n_vogais += 1

print("A palavra", palavra, "possui", num_vogais, "vogais.")
