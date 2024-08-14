#OrientacaoObj

#Paradigma imperativo

def registrar(nome, idade, cpf, email):
    paciente = {"nome": nome, "idade": idade, "cpf": cpf, "email": email}
    return paciente


#Paradigma orientado a objeto

class Paciente: 
    
    def __init__(self, nome, idade, cpf, email):
        print("Acessei meu construtor")
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.email = email 