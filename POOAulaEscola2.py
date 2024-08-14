#POOAulaEscola2
from abc import ABC, abstractmethod

# superclasse
class Pessoa(ABC):
    
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Classe Pessoa")
        
        
    def imprimir_nome(self):
        return self.nome

    
    @abstractmethod
    def trabalhar(self):
        pass

class Administrador(Pessoa):
    
    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return f"Classe {nome_classe} Organizando planilhas"
        

#subclasse
class Aluno(Pessoa):
    
    def __init__(self, nome):
        super().__init__(nome)    
        self.matricula = None
        self.notas = []
        print("Classe Aluno")
        
        
    def estudar(self):
        return "Estudando"
    

#subclasse
class Professor(Pessoa):
    
    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []
        
        
    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return f"Classe {nome_classe} ensinando"
    
    
professor = Professor("Marcos")