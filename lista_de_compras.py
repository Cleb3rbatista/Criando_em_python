mylist = []
def lista():
    escolha = input("Escolha uma das opções " \
                    "[I]serir, [E]xcluir, [M]ostrar lista, [S]ubistituir ou [L]impar\n").upper()

    if escolha == "I":
        laco_insert = True
        while laco_insert:
            insert_produto = input("Digite o produto que deseja incluir na lista de compra:\n")
            mylist.append(insert_produto)
            laco_insert_itermediario = True
            incluir_novamente = input("Deseja incluir mais produtos?\n [S]im ou N[ão]\n").upper()
            if incluir_novamente == "S":
                continue
            elif incluir_novamente == "N":
                for indice , produto in enumerate(mylist , start=1):
                    print( indice , produto)
                    continue
                while True:
                    insert_fim= input("deseja concluir a sua lista?\n [S]im ou [N]ão\n").upper()
                    if insert_fim == "S":
                        print("lista concluida com sucesso")
                        exit()
                    elif insert_fim == "N":
                        lista()
                    else:
                        print("opção invalida!")
                        continue
            else:
                print("Opção digitada e invalida!")
                continue
    elif escolha == "E":
        if mylist == '':
            print("não a o que excluir na lista")
            lista()
        else:
            laco_delet = True
            while laco_delet:
                delet_produto = input("o nome do produto que deseja excluir da lista\n")
                if mylist.count(delet_produto) == 0:
                    print(" produto não pertece a lista")
                    continue
                if mylist.count(delet_produto) != 0:
                    mylist.remove(delet_produto)
                    print("produto excluido com sucesso")
                    laco_deler_itermediario = True
                    while laco_deler_itermediario:
                        delet_novamente = input("Deseja deletar mais produtos?\n [S]im ou [N]ão\n").upper()
                        if delet_novamente == "S":
                            continue
                        elif delet_novamente == "N":
                            for indice, produto in enumerate(mylist, start=1):
                                print(indice, produto)
                        else:
                            print(" opção invalida!")
                            continue
                        while True:
                            delet_fim = input("Deseja concluir a lista?\n [S]im ou [N]ão\n").upper()
                            if delet_fim == "S":
                                print("Lista concluida com sucesso")
                                exit()
                            elif delet_fim == "N":
                                lista()
                            else:
                                print("opção invalida!")
                                continue
                    else:
                        print("opção digitada invalida!")
                        break
    elif escolha == "M":
        if mylist == '':
            print(" A lista esta Vazia")
            lista()
        else:
            for indice, produto in enumerate(mylist, start= 1):
                print(indice,produto)
                continue
            lista()
    elif escolha == "L":
        if mylist == '':
            print(" A lista esta vazia")
        else:
            confirma_lipeza = input("deseja mesmo excluir todos os produtos da lista?\n [S]im ou [N]ão\n").upper()
            if confirma_lipeza == "S":
                mylist.clear()
                print("lista limpa com sucesso")
                criar_nova_lista = input("Deseja criar uma nova lista?\n [S]im ou [N]ão\n").upper()
                while True:    
                    if criar_nova_lista == "S":
                        lista()
                    elif criar_nova_lista == "N":
                        print("saindo...")
                        exit()
                    else:
                        print("opção invalida!")
                        continue
    elif escolha == "S":
        if mylist == '':
            print("não tem oque substituir")
            lista()
        else:
            while True:
                substituir_produto = input("Digite o nome do produto que deseja substituir\n")
                if mylist.count(substituir_produto)== 0:
                    print("não existe esse produto na lista")
                    continue
                elif mylist.count(substituir_produto) != 0:
                    novo_produto = input("digite o nome do novo produto\n")
                    if mylist.count(novo_produto) != 0:
                        print(" esse produto ja esta na lista")
                        continue
                    elif mylist.count(novo_produto) == 0:
                        mylist[mylist.index(substituir_produto)]= novo_produto
                        print("produto substituido com sucesso")
                        lista()
    else:
        print(" opção invalida!")
        lista()          
lista()