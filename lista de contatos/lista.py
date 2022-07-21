lista_contatos = [["Pedro", 21, "19999999999"], ["Joao", 23, "19995699978"]]
while True:
    print("""Lista de Pessoas
    1 - Adcionar uma pessoa.
    2 - Mostrar a lista.
    3 - Editar a lista.
    4 - Excluir uma pessoa.
    5 - Sair.""")
    opc = int(input("Dígite a opção que deseja: "))
    if opc == 1:
        nome = str(input("Dígite o nome da pessoa a adcionar: ")).capitalize()
        idade = int(input("Dígite a idade dessa pessoa: "))
        tel = str(input("Qual é o telefone de contanto dessa pessoa: "))
        pessoa = [nome, idade, tel]
        lista_contatos.append(pessoa)
    elif opc == 2:
        for p in lista_contatos:
            print(f"""Nome: {p[0]}
            Idade: {p[1]}
            Telefone: {p[2]}""")
    elif opc == 3:
        while True:
            ind = str(input("Nome da pessoa que deseja editar? ")).capitalize()
            pos = None
            for i in range(len(lista_contatos)):
                if lista_contatos[i][0] == ind:
                    pos = i
            if pos != None:
                break
        print("""1 - Nome.
        2 - Idade.
        3 - Telefone""")
        edi = int(input("Qual infomação voce deseja editar? "))
        if edi == 1:
            lista_contatos[pos][0] = str(input("Qual sera o nome dessa pessoa? ")).capitalize()
        elif edi == 2:
            lista_contatos[pos][1] = int(input("Qual sera a idade dessa pessoa? "))
        elif edi == 3:
            lista_contatos[pos][2] = str(input("Qual sera o telefone dessa pessoa? "))
    elif opc == 4:
        while True:
            ind = str(input("Nome da pessoa que você deseja retirar da lista? ")).capitalize()
            pos = None
            for i in range(len(lista_contatos)):
                if lista_contatos[i][0] == ind:
                    pos = i
            if pos != None:
                break
        lista_contatos.pop(pos)
    elif opc == 5:
        break