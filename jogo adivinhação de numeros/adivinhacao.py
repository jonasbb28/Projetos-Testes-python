from random import randint

print("""Vamos jogar um jogo?
Vou escolher um número entre 1 e 20.
Você tera 5 chances de acertar o meu número.
Vamos lá!""")
acertos = erros = 0
while True:
    numero = randint(1, 20)
    for t in range(1, 6):
        palpite = int(input(f"{t}° tentativa: "))
        if palpite == numero:
            print("Parabéns! Você acertou o meu número.")
            acertos += 1
            break
        elif t == 5:
            print(f"Ops! Você não conseguiu adivinhar o meu número, eu estava pensndo no número {numero}.")
            erros += 1
        maior = palpite
        menor = numero
        if numero > maior:
            maior = numero
            menor = palpite
        if (maior-menor) >= 7: 
            print("Muito Frio!")
        elif (maior-menor) >= 5:
            print("Frio!")
        elif (maior-menor) >= 3:
            print("Quente!")
        elif (maior-menor) > 0:
            print("Muito Quente!")
    res = str(input("Você quer adivinhar de novo? [S/N]")).upper()
    if res == "N":
        break

print(f"""Placar do jogo!
Você acertou: {acertos}
Você errou: {erros}""")

