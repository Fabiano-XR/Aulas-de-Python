import random, time, os, sys #, keyboard
programas = []

pasta = os.path.dirname(sys.executable)
for p in os.listdir(pasta):
    programas.append(p[:-4].title())
for programa in programas:
    print(f"{programa}")

escolhido = random.choice(programas)
print(f"Executando {escolhido}...")# \n Se desejar abrir outro aperte qualquer tecla em 5")

time.sleep(3)
os.startfile(os.path.join(pasta, escolhido))

#escolher_outro = False

#for i in range (4, 0, -1):
#    time.sleep(1)
#    print(f"Aperte qualquer tecla em {i}")
    