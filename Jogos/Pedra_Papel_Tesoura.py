import random
lose = win = user = 0

print ("!Iniciar jogo!")
print("Regras: digite pedra, papel ou tesoura (ou zero para encerrar o jogo.)")

def RandomChoise():
    var = random.randint(1, 3)
    if var == 1:
        return "pedra"
    elif var == 2:
        return "tesoura"
    elif var == 3:
        return "papel"

while user != "zero":
    user = input("escolha: ").lower()
    if user != "pedra" or "papel" or "tesoura" or "zero":
        print("Digite algo valido! \n (Pedra, papel, tesoura ou zero para encerrar.)")
    machine = RandomChoise()
    
    if user == machine:
        print("Empate")

    elif user == "pedra" and machine == "papel":
        print("Perdeu")
        lose += 1
    elif user == "tesoura" and machine == "pedra":
        print("Perdeu")
        lose += 1
    elif user == "papel" and machine == "tesoura":
        print("Perdeu")
        lose += 1
    elif user == "pedra" and machine == "tesoura":
        print("Ganhou")
        win += 1
    elif user == "tesoura" and machine == "papel":
        print("Ganhou")
        win += 1
    elif user == "papel" and machine == "pedra":
        print("Ganhou")
        win += 1

print("fim de jogo")
print(f"Maquina {lose} X {win} Usuario")


#pedra 1 
#tesoura 2
#papel 3