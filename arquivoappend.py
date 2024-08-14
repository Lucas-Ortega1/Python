#arquivoappend

texto = "caramelo"

with open ("receita.txt", "a") as arquivo:
    arquivo.write("\n")
    arquivo.write(texto)