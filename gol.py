time1 = int(input("Digite o gol do primeiro time:"))
time2 = int(input("Digite o gol do segundo time:"))

if time1 > time2:
    print("Time 1 ganhou o jogo")
else:
    if time2 > time1:
        print("Time 2 ganhou o jogo")
    else:
        print("O jogo empatou")


