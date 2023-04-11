p = input("Digite uma palavra: ")
vo = 'aeiou'
n_vogais = 0

for letra in p:
    if letra.lower() in vo:
        n_vogais += 1

substituir = input("Digite um caractere para substituir as vogais: ")

nova_palavra = ""
for letra in p:
    if letra.lower() in vo:
        nova_palavra += substituir
    else:
        nova_palavra += letra

print("A palavra", p, "possui", n_vogais, "vogais.")
print("Nova palavra:", nova_palavra)
