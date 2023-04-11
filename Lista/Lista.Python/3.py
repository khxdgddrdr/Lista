vA = list("COMPUTACAO")

vB = input("Digite uma palavra de 10 letras: ")

vB = vB.upper()

for i in range(len(vetA)):
    if vA[i] == vB[i]:
        print(f"A letra '{vB[i]}' está na posição {i} de vetB.")

vA = "COMPUTACAO"
vB = input("Digite uma palavra de 10 letras: ")

print("As letras em comum nas mesmas posições são:")
for i in range(len(vA)):
    if vetA[i].lower() == vB[i].lower():
        print(i, end=" ")
print()

print("A palavra digitada foi:", vB)

string = input("Digite uma string: ")
comprimento = len(string)
print("O comprimento da string é:", comprimento)
