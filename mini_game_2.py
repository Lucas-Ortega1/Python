from random import choice

vitorias_jogador = 0
vitorias_maquina = 0
empates = 0

def opcao_jogador():
    PPT_jogador = input("Escolha pedra, papel ou tesoura: ")
    if PPT_jogador == "pedra":
        return PPT_jogador
    elif PPT_jogador == "papel":
        return PPT_jogador
    elif PPT_jogador == "tesoura":
        return PPT_jogador
    else:
        print("Opcao invalida!!!")
        opcao_jogador()

def opcao_maquina():
    PPT_maquina = choice(["pedra", "papel", "tesoura"])
    return PPT_maquina    



while True:
    
    print("-"*20)
    print("BEM VINDO AO JOGO PEDRA, PAPEL OU TESOURA!!!")
    print("-"*20)

    print("-"*20)
    print("\nVitorias do jogador: ", vitorias_jogador)
    print("Vitorias da maquina: ", vitorias_maquina)
    print("Empates: ", empates)
    print("-"*20)     
       
    PPT_jogador = opcao_jogador()
    PPT_maquina = opcao_maquina()
    
    #jogador ganha
    if (PPT_jogador == "pedra") and (PPT_maquina == "tesoura") \
        or (PPT_jogador == "papel") and (PPT_maquina == "pedra") \
            or (PPT_jogador == "tesoura") and (PPT_maquina == "papel"):
                print("Jogador escolheu ", PPT_jogador, " e a maquina escolheu ", PPT_maquina)
                print("Vitoria do jogador")
                vitorias_jogador = vitorias_jogador + 1
    
    #empate            
    elif PPT_jogador == PPT_maquina:
        print("Jogador escolheu ", PPT_jogador, " e a maquina escolheu ", PPT_maquina)
        empates = empates + 1
    
    #maquina ganha            
    else:
        print("Jogador escolheu ", PPT_jogador, " e a maquina escolheu ", PPT_maquina)
        print("Vitoria da maquina")
        vitorias_maquina = vitorias_maquina + 1
                
    
    esc_jogador = input("Quer jogar novamente?(S/N): ")
    if esc_jogador == "S":
        pass
    elif esc_jogador == "N":
        break
    else:
        print("Opcao invakida!")
        
        