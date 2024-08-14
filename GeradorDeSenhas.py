
chave = input("Digite a senha que quer utilizar: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "@"
    elif letra in "Ee":
        senha = senha + "&"
    elif letra in "Ii":
        senha = senha + "1"
    elif letra in "Oo":
        senha = senha + "0"
    elif letra in "Ss":
        senha = senha + "$"             
    else: senha = senha + letra    

print("Sua nova senha eh: ",senha)