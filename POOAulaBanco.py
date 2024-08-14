#POOAulaBanco

class Conta:
    
    #Atributo de classe
    taxa = 0.50
    
    #metodo da classe
    """@classmethod
    def retornarcodigo(cls):
        print("Codigo: 555")"""
    
    
    #metodo estatico
    @staticmethod
    def retornarCodigoBanco():
        return "345"
    
    #Atributos de instâncias
    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero #visibilidade protegida
        self.titular = titular #visibilidade publica
        self.__saldo = saldo #visibilidade privada
        self.__historico = [saldo]
        
    
    def saldo(self):
        print("Saldo: R$", self.__saldo)
        
        
    def transacao(self, saldo):
        self.__historico.append(saldo)
        
        
    def extrato(self):
        print("-------EXTRATO-------")
        print("Conta: ",self.titular)
        for saldo in self.__historico:
            print("Saldo: R$", self.__saldo)
    
    
    def depositar(self, deposito):
        self.__saldo = self.__saldo + deposito
        self.transacao(self.__saldo)
        
        
    def sacar(self, valor):
        self.__saldo = self.__saldo - valor
        self.transacao(self.__saldo)
        
            
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        
conta1 = Conta(123, "Roberto", 2300)
conta2 = Conta(456, "Maria")