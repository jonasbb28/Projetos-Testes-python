from random import randint
palavras = ["bricadeiro", "leite", "cafe", "escola", "universidade", "faculdade"]
palavra = palavras[randint(0, len(palavras)-1)].lower()
copia = []
letras = []
erros = 1
print("Vamos brincar de forca?")
print("Você tera 8 chances para chutar uma letra, se não o seu jogador sera enforcado")
for i in range(len(palavra)):
    copia.append("_")
while True:
    letra = str(input("Qual letra você ira chutar: ")).lower()
    if letra in letras:
        print(f"A letra {letra} já foi escolhida!")
        continue
    if letra not in letras:
        letras.append(letra)
    if letra in palavra:
        for i in range(len(copia)):
            if palavra[i] == letra:
                copia[i] = letra
    elif letra not in palavra:
        print(f"Essa letra não faz parte da palavra! Você tem mais {8 - erros} chances")
        erros += 1
        continue
    if erros == 8:
        print("Ops! Suas chances acabaram")
        print(f"A palavra era {palavra}.")
        break
    if "".join(copia) == palavra:
        print("Parabens! Você conseguiu acertar a palavra!")
        break
    for l in copia:
        print(f"{l}", end="")
    print()
        
