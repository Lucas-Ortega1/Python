
numero = int(input("Insira um numero para descobrir se ele eh um numero primo: "))
contador = 0

if numero <= 1:
    print("Numero invalido")
else:
    for x in range(1,numero+1):
        if numero % x == 0:
            contador = contador + 1

if contador <= 2:
    print("O numero ", numero, " eh primo.")
else:
    print("O numero ", numero, " nao eh primo.")