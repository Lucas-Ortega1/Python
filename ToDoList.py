#ToDoList


tarefas = []
tarefas_listadas = list(enumerate(tarefas, start=1))
continuar = "sim"

def exibir_itens():
    return print(tarefas_listadas)


def adicionar_final():
    resposta = input("Item a adicionar: ")
    tarefas.append(resposta)
    return tarefas


def adicionar_inicio():
    resposta = input("Item a adicionar: ")
    tarefas.insert(0,resposta)
    return tarefas


def eliminar_item1():
    if tarefas:
        tarefas.pop(0)
    return tarefas

def eliminar_qualquer(new):
    if tarefas:
        resposta = input("Item a eliminar: ")
        tarefas.pop(resposta+1)
    return tarefas    

def esvaziar_lista():
    tarefas.clear
    return tarefas
    
    
    
while continuar != "nao":
        print("===========================MENU==========================\n")
        print("Anote aqui as suas tarefas a faazer")
        print("OBS: Anote sues itens na ordem de prioridade decrescente\n\n")
        print("1 - Imprimir lista")
        print("2 - Adicionar item no início")
        print("3 - Adicionar item no final")
        print("4 - Eliminar primeiro item(elimina sempre o primeiro item)")
        print("5 - Escolher item para eliminar")
        print("6 - Esvaziar lista\n\n")
        
        opcao = int(input("Selecione uma das opcoes acima: "))
        
        if opcao == 1:
            exibir_itens()
        if opcao == 2:
            adicionar_inicio()
        if opcao == 3:
            adicionar_final()
        if opcao == 4:
            eliminar_item1()
        if opcao == 5:
            eliminar_qualquer()
        if opcao == 6:
            esvaziar_lista()
            
        novo_continuar = input("Quer continuar? ")
        continuar = novo_continuar      
        
            
            
    

