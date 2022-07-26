from random import choice

def linha(quant):
    print("-"*quant)


def exibir(rebo, voce):
    linha(20)
    print(f"A minha escolha {rebo}")
    print(f"A sua escolheu {voce}")
    linha(20)


escolhas = ["pedra", "papel", "tesoura"]
print("""Vamos brincar de pedra, papel e tesoura!
Vamos fazer um jogo com 3 rodadas, quem ganhar duas será o vencedor!
Vamos nessa!!""")
g = p = e = 0
for i in range(1, 6):
    print(f"{i}° Rodada:")
    escolha = choice(escolhas)
    res = str(input("Qual você vai jogar: ")).lower()
    if res == "pedra" and escolha == "tesoura" or res == "papel" and escolha == "pedra" or res == "tesoura" and escolha == "papel":
        exibir(escolha, res)
        print(f"Você ganhou a {i}° rodada.")
        linha(20)
        g += 1
    elif res == "pedra" and escolha == "papel" or res == "papel" and escolha == "tesoura" or res == "tesoura" and escolha == "pedra":
        exibir(escolha, res)
        print(f"Você perdeu a {i}° rodada.")
        linha(20)
        p += 1
    elif res == escolha:
        exibir(escolha, res)
        print(f"Ocorreu um empante na {i}° rodada.")
        linha(20)
        e += 1

print("Agora vamos ver quem ganhou o jogo:")
print(f"Eu ganhei {p} rodada(s).")
print(f"Você ganhou {g} rodada(s).")
if e > 0:
    print(f"Ocorreu {e} empate(s).")
if g > p and g > e:
    print("Você ganhou!")
elif p > g and p > e:
    print("Você perdeu!")
else:
    print("Acabou em empate")