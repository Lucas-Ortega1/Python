#arquivotestePDF

import pydf

pdf = pydf.generate_pdf('<h1>Ola mundo</h1><p>Testando meu documento<\p>')

with open('meuarquivo.pdf', 'wb') as arquivo:
    arquivo.write(pdf)
