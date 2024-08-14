valor_inicial = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto(%): "))

desconto = desconto / 100

valor_final = valor_inicial - (valor_inicial * desconto)

print("O valor final do produto eh: ",valor_final)