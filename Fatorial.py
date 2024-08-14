
print("-----BEM VINDO A CALCULADORA FATORIAL-----")

fat = int(input("Qual fatorial voce quer conhecer: "))
aux = 1
resultado = 1

if fat > 0:
    while aux <= fat:
        resultado = resultado * aux
        aux = aux + 1

    print("O resultado eh: ",resultado)
elif fat == 0:
    print("O fatorial de 0 eh 1")    
else:
    print("Nao eh possivel calcular o fatorial de numeros negativos")    