print("Bem vindo a calculadora inteligente de IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura**2
print("Seu IMC eh: ",imc)

if imc <= 16.9:
    print("Seu IMC eh muito abaixo do peso")
elif imc > 16.9 and imc <= 18.4:
    print("Seu IMC eh abaixo do peso") 
elif  imc > 18.4 and imc <= 24.9:
    print("Seu IMC está normal")
elif  imc > 24.9 and imc <= 29.9:
    print("Seu IMC está acima do peso")
elif  imc > 29.9 and imc <= 34.9:
    print("Seu IMC está em obesidade grau 1")
elif  imc > 34.9 and imc <= 40:
    print("Seu IMC está em obesidade grau 2")
else:
    print("Seu IMC está em obesidade grau 3")

print("Obrigado por usar a calculadora inteligente de IMC!")    
