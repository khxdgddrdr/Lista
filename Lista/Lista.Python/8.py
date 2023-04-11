n = input("Digite o nome da pessoa: ")
s = input("Digite o sexo da pessoa (M ou F): ")
i = int(input("Digite a idade da pessoa: "))

if s == "F" and i < 25:
    print(n + " ACEITA")
else:
    print("NÃO ACEITA")
