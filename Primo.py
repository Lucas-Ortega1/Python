#VERIFICADOR DE NUMERO PRIMO
def primo(numero):
    cont = 0
    if numero <= 1:
        print("Esse numero nao eh primo, numero menor ou igual a 1")
    else:
        for x in range(1,numero+1):
            if (numero % x) == 0:
                cont = cont + 1
        if cont == 2:
            print("O numero ", numero, " eh primo.")
        else:
            print("O numero ", numero, " nao eh primo.")


