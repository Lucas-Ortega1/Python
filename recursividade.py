#recursividade

'''def recursao(numero):
    print(numero)
    if numero < 0:
        return -1
    elif numero == 0:
        return 0
    else:
        return recursao(numero - 1)

   
recursao(10)'''

#FATORIAL SEM RECURSAO
#modo que eu fiz
'''def fatorialS(numero):
    fat = 1
    while numero > 0:
        fat = fat * numero
        numero = numero -1
    print("O fatorial de ",numero, " eh ",fat)'''

#modo que o curso fez
'''def fatorialS(numero):
    fatorial = 1
    if numero == o:
        return 1
    else:
        for x in range(1, numero +1):
            fatorial = fatorial * x
        return fatorial    

print(fatorialS(6))'''

#FATORIAL COM RECURSAO

def fatorialR(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorialR(numero -1) 

print(fatorialR(5))


