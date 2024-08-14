#POOAulaEscola
#Aula getters e setters

class Aluno:
    
    def __init__(self, nome, idade, matricula):
        self.__nome = nome 
        self._idade = idade
        self.matricula = matricula
        self.notas = None
        
        
    def nome(self):
        return self.__nome   
        
        
    def set_nome(self, nome):
        self.__nome = nome
        
        
    def get_idade(self):
        return self._idade
        
        
    def idade(self, idade):
        self._idade = idade
        
        
aluno1 = Aluno("Marcos", 15, 123456)
print(aluno1.nome())


'''print(aluno1.get_idade())
print(aluno1.matricula) 
print(aluno1.notas)'''