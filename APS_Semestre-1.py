while True:
    try:
        exer = int(input("digite o numero do exercicio que deseja (0 - Encerrar): "))
        break
    except:
        print("Valor invalido.")
if (exer == 0):
    print("Até a proxima.")

#1. Desenvolva um programa que calcule a média de duas notas de 25 alunos, e no final mostre quantos alunos foram APROVADOS, sabendo que o aluno estará aprovado com a média aritmética maior ou igual a 6,0.
elif (exer == 1):
    aproved = reproved = 0
    while True:
        for i in range (25):
            i+=1
            try:
                nota = float(input(f"Digite a 1° nota do {i}° aluno: "))
            except:
                print("Entrada invalida.")
            try:
                nota += float(input(f"Digite a 2° nota do {i}° aluno: ")) 
            except:
                print("Entrada invalida.")
            med = nota/2
            if med >= 6:
                aproved+=1
            else:
                reproved+=1
        break
    print(f"O numero de alunos aprovado é {aproved} e o de reprovados é {reproved}.")

#2. Desenvolva um programa que leia o nome do aluno e duas notas, em seguida mostre na tela o Nome do aluno e se está Aprovado ou Reprovado. (Aprovado se média aritmética for maior ou igual a 6,0.)
elif (exer == 2):
    nota = 0
    nome = str(input("Digite o nome do aluno: "))
    for i in range(2):
        try:
            i+=1
            nota += float(input(f"Digite a {i}° nota do aluno: ")) 
        except:
            print("Entrada invalida.")
    med = nota/2
    if med >= 6:
        print(f"O aluno(a) {nome} foi Aprovado! Com media de {med:.1f}")
    else:
        print(f"O aluno(a) {nome} foi Reprovado! Com media de {med:.1f}")

#3. Desenvolva um programa que leia a idade de 40 alunos, e no final mostre a quantidade de alunos maiores que 18 anos.
elif (exer == 3):
    import random
    adulto = adulto_alt = 0
    def manual():
        while True:
            try:
                temp = int(input(f"Digite a idade do {i}° aluno: "))
                return temp
            except:
                print("Entrada invalida.")
    def aleatorio(min, max):
        temp = random.randint(min, max)
        return temp

    while True:
        try:
            tip = int(input("Deseja inserir os numeros manualmente ou gerar de forma aleatoria? \n 1 - Manual. \n 2- aleatorio. \n ....."))
        except:
            print("Entrada invalida.")
        if tip == 1 or tip ==2:
            break
    
    if tip ==2:
        min = int(input(f"Digite a idade minima dos alunos: "))
        max = int(input(f"Digite a idade maxima dos alunos: "))
    for i in range(40):
        i +=1
        while True:
            if tip == 1:
                idade = manual()
            else:
                idade = aleatorio(min, max)
            if idade >= 18:
                adulto+=1
            if idade > 18:
                adulto_alt+=1
            print(f"{i}° aluno tem {idade} anos.")
            break

    print(f"A quantidade de alunos maior que 18 anos é {adulto_alt}.\n E a quantidade de alunos maiores de idade é {adulto}.")



else: #FIM DO CODIGO
    print("Não tem esse exercicio.")