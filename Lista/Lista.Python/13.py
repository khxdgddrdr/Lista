stri = input("Digite uma palavra ou frase: ")

n_string = ""

for let in stri:
    if let.lower() not in "aeiou":
        n_string += let

print("A nova string sem vogais é:", n_string)
