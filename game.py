import random

#Aqui O jogador irá escolher a sua jogada
print("Escolha Pedra, Papel ou Tesoura")
Player = input("Digite sua escolha: ")

#Transforma todos os caracteres em minúsculo (Evitar erros de entrada do usuário)
Player = Player.lower()

#Transforma a jogada do player para números (Mais fácil de ser manipulado)
if Player == "pedra":
    P1 = 1
if Player == "papel":
    P1 = 2
if Player == "tesoura":
    P1 = 3

#O programa faz a sua escolha
P2 = random.randint(1,3)

#O programa começa a entender quem ganhou
if P1 == P2:
    print("Empate")

#P1 = Pedra
elif P1 == 1 and P2 == 2:
    print ("CPU Venceu")
elif P1 == 1 and P2 == 3:
    print ("Jogador Venceu")

#P1 = Papel   
elif P1 == 2 and P2 == 1:
    print("Jogador Venceu")
elif P1 == 2 and P2 == 3:
    print("CPU Venceu")

#P1 = Tesoura
elif P1 == 3 and P2 == 1:
    print("CPU Venceu")
elif P1 == 3 and P2 == 2:
    print("Jogador Venceu")







