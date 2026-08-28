import random
lose = win = user = 0

print ("!iniciar jogo!")
print("Regras: digite pedra, papel ou tesoura (ou zero para encerrar o jogo.)")
#def RandomChoise(user)
    

    

while user != "zero":
    user = input("escolha: ")
    maquina = random.randint(1, 3)
    if user == "pedra" and maquina == 1:
        print("Empate")
    elif user == "tesoura" and maquina == 2:
        print("Empate")
    elif user == "papel" and maquina == 3:
        print("Empate")
    elif user == "pedra" and maquina == 3:
        print("Perdeu")
        lose += 1
    elif user == "tesoura" and maquina == 1:
        print("Perdeu")
        lose += 1
    elif user == "papel" and maquina == 2:
        print("Perdeu")
        lose += 1
    elif user == "pedra" and maquina == 2:
        print("Ganhou")
        win += 1
    elif user == "tesoura" and maquina == 3:
        print("Ganhou")
        win += 1
    elif user == "papel" and maquina == 1:
        print("Ganhou")
        win += 1

print("fim de jogo")
print(f"Maquina {lose} X {win} Usuario")


#pedra 1 
#tesoura 2
#papel 3