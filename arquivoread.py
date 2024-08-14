#arquivoread

#arquivo = open("receita.txt")
#print(arquivo.closed)
#print(arquivo.read())

#arquivo.close()

with open("receita.txt") as arquivo:
    print(arquivo.read())
    print(arquivo.closed)
print(arquivo.closed)
    

