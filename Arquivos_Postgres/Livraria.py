import psycopg2
import os

conexao = psycopg2.connect(host='localhost', 
                        database='Biblioteca',
                        user='postgres', 
                        password='postgres')

cursor = conexao.cursor()

def volta_ao_menu():
    print()
    while True:
        opcao_volta_menu = input("Deseja volta ao menu ?\n[S]im ou [N]ão\n").upper()
        if opcao_volta_menu == "S":
            os.system("cls")
            menu()
        elif opcao_volta_menu == "N":
            print("Saindo...")
            exit()
        else:
            print()
            print("opção invalida!\n tente novamente")
            print()
            continue

def comprar_livros():
    while True:
        deseja_comprar = input("Deseja comprar um livro?\n [S]im ou [N]ão\n").upper()
        if deseja_comprar == "N":
            print("Saindo...")
            exit()
            
        elif deseja_comprar == "S":
            while True:
                try:
                    idlivro_escolhido = int(input("Qual o numero do livro que voce deseja comprar?\n"))
                    if idlivro_escolhido <= 0:
                        print("A lista começa do livro de numero 1\n tente novamente\n")
                        continue
                    cursor.execute(f"SELECT id_livros  FROM public.livros")
                    qtd_livros =len(cursor.fetchall())
                    if idlivro_escolhido > qtd_livros:
                        print(f"Atualmente a somete {qtd_livros} na biblioteca\n tente navamente!\n")
                        continue
                except ValueError:
                    
                    print()
                    print("Digite um numero inteiro\n tente novamente")
                    print()
                    continue
                else:
                    break
            
        else:
            print()
            print("opção invalida!\n tente novamente")
            print()
            continue
            
        cursor.execute(f"SELECT *  FROM public.livros WHERE id_livros = '{idlivro_escolhido}'")
        
        for livro_para_comprar in cursor.fetchall():
            if livro_para_comprar[7] == True:
                print("o livro esta inativo!")
                volta_ao_menu()
            while True:
                confirmando_livro = input(f"O livro escolhido e {livro_para_comprar[1]}?\n [S]im ou [N]ão\n").upper()

                if confirmando_livro == "S":
                    print(f"O livro {livro_para_comprar[1]} custa {livro_para_comprar[6]}")
                    print("Boa leitura!")
                    volta_ao_menu()
                    
                elif confirmando_livro == "N":
                    while True:
                        escolher_novamente=input("lamento, deseja escolher novamente?\n [S]im ou [N]ão\n").upper()
                        
                        if escolher_novamente == "S":
                            os.system("cls")
                            comprar_livros()
                            
                        elif escolher_novamente == "N":
                            print("Saindo...")
                            exit()
                            
                        else:
                            print()
                            print("opção invalida!\n tente novamente")
                            print()
                            continue
                else:
                    print()
                    print("opção invalida!\n tente novamente")
                    print()
                    continue       
                
def busca_de_livros():
    cursor.execute("SELECT id_livros , livro ,preco FROM public.livros WHERE inativo = false ORDER BY id_livros, id_livros ASC")
    for linha in cursor.fetchall():
        print(f" {linha[0]}) {linha[1]} preço: {linha[2]},")

def incluir_novos_livros():
    while True:
        nome_do_novo_livro =input ("Qual e o nome do livro novo?\n")
        if len(nome_do_novo_livro) >= 5:
            while True:
                nome_do_novo_autor = input("Qual o nome do autor?\n")
                if len(nome_do_novo_autor) >= 3:
                    while True:
                        sexo_do_novo_autor = input("Qual o sexo do autor?\n[M]asculino ou [F]eminino\n").upper()
                        if sexo_do_novo_autor == 'M' or 'F':
                            while True:
                                try:
                                    ano_do_livro_novo = int(input("Qual e o ano de publicação do livro?\n"))
                                except ValueError:
                                    print("\nDigite um numero inteiro\ntente novamente\n")
                                    continue
                                while True:
                                    descricao_do_novo_livro = input("Digite a descrição do livro novo (Maximo 2000 caracteres)\n")
                                    if len(descricao_do_novo_livro) == 0 and len(descricao_do_novo_livro) > 2000:
                                        print("Quantidade de caracteres e invalido\n Tente novamente\n")
                                    else:
                                        while True: 
                                            try:
                                                preco_do_novo_livro = float(input("Digite o preço do livro\n"))
                                            except ValueError:
                                                print("\n o valot teve ser um numero real!\n EX: 18.90 ou 18\n tente novamete\n")
                                                continue
                                        
                                            if preco_do_novo_livro <= 0:
                                                print("\nO preço deve ser maior que zero!\ntente novamente\n")
                                                continue    

                                            cursor.execute(f"INSERT INTO livros(livro, autor, sexo_do_autor, ano_de_lancamento, descricao, preco, inativo) VALUES ('{nome_do_novo_livro}', '{nome_do_novo_autor}', '{sexo_do_novo_autor}', {ano_do_livro_novo}, '{descricao_do_novo_livro}',{preco_do_novo_livro}, 'false');")
                                            conexao.commit()
                                            print("livro cadastrado com sucesso")
                                            volta_ao_menu()                 
                        else:
                            print("Opção invalida\n tente novamente\n")
                            continue
                elif len(nome_do_novo_autor) <3:
                    print("O nome do autor deve conter no minimo 3 caracters\n")
                    continue
                    
        else:
            print("O nome do livro deve conter no minimo 5 caracters\n")
            continue
                                    
def altera_preco_livro():
    while True:
        try:
            livro_para_alterar_preco = int(input("Qual e o código do livro ?\n"))
            if livro_para_alterar_preco <= 0:
                print("A lista começa do livro de numero 1\n tente novamente\n")
                continue
            cursor.execute(f"SELECT id_livros  FROM public.livros")
            qtd_livros =len(cursor.fetchall())
            if livro_para_alterar_preco > qtd_livros:
                print(f"Atualmente a somete {qtd_livros} na biblioteca\n tente navamente!\n")
                continue
        except ValueError:
            print("\ndigite um valor inteiro!\ntente novamente\n")
            continue
        cursor.execute(f"SELECT livro, autor, ano_de_lancamento ,preco FROM livros WHERE id_livros='{livro_para_alterar_preco}'")
        for linha in cursor.fetchall():
            while True:
                confirmando_livro = input(f"O livro escolhido e {linha[0]} lançado em {linha[2]} por {linha[1]} o preço atual e de {linha[3]}\nDesja altera o preço do livro?\n [S]im ou [N]ão\n").upper()
                if confirmando_livro == 'N':
                    print("ops!")
                    volta_ao_menu()
                elif confirmando_livro == 'S':
                    preco_novo = input("\nQual e o preço novo ?\n")
                    cursor.execute(f"UPDATE livros SET preco={preco_novo} WHERE id_livros = '{livro_para_alterar_preco}';")
                    conexao.commit()
                    volta_ao_menu()
                else:
                    print("\nOpção invalida!\n tente novamente\n")
                    continue
                
def ler_descricao():
    while True:
            try:
                livro_para_ler_descricao = int(input("Qual e o código do livro ?\n"))
                if livro_para_ler_descricao <= 0:
                    print("A lista começa do livro de numero 1\n tente novamente\n")
                    continue
                cursor.execute(f"SELECT id_livros  FROM public.livros")
                qtd_livros =len(cursor.fetchall())
                if livro_para_ler_descricao > qtd_livros:
                    print(f"Atualmente a somete {qtd_livros} na biblioteca\n tente novamente!\n")
                    continue
            except ValueError:
                print("\ndigite um valor inteiro!\ntente novamente\n")
                continue
            
            cursor.execute(f"SELECT livro, descricao FROM livros WHERE id_livros = '{livro_para_ler_descricao}'")
            for linha in cursor.fetchall():
                print(f"Livro: {linha[0]}\nDescrição: {linha[1]}\n") 
                volta_ao_menu()      
def inativa_livro():
     while True:
            try:
                livro_para_inativar = int(input("Qual e o código do livro ?\n"))
                if livro_para_inativar <= 0:
                    print("A lista começa do livro de numero 1\n tente novamente\n")
                    continue
                cursor.execute(f"SELECT id_livros  FROM public.livros")
                qtd_livros =len(cursor.fetchall())
                if livro_para_inativar > qtd_livros:
                    print(f"Atualmente a somete {qtd_livros} na biblioteca\n tente novamente!\n")
                    continue
            except ValueError:
                print("\ndigite um valor inteiro!\ntente novamente\n")
                continue
            
            cursor.execute(f"SELECT livro , inativo FROM livros WHERE id_livros = '{livro_para_inativar}'")
            for linha in cursor.fetchall():
                if linha[1] == False:
                    print("\nO livro não esta inativo")
                    while True:
                        deseja_inativar = input("Deseja inativar o livro ?\n[S]im ou [N]ão\n").upper()
                        if deseja_inativar == 'N':
                            volta_ao_menu()
                        elif deseja_inativar == 'S': 
                            cursor.execute(f"UPDATE livros SET inativo = true WHERE id_livros = '{livro_para_inativar}';")
                            conexao.commit()
                            volta_ao_menu()
                        else:
                            print("Opção invalida!\ntente novamente\n")
                            continue
                        
                elif linha[1] == True:
                    print("O livro esta inativo")
                    while True:
                        deseja_ativar = input("Deseja ativar o livro ?\n[S]im ou [N]ão\n").upper()
                        if deseja_ativar == 'N':
                            volta_ao_menu()
                        elif deseja_ativar == 'S': 
                            cursor.execute(f"UPDATE livros SET inativo = false WHERE id_livros = '{livro_para_inativar}';")
                            conexao.commit()
                            volta_ao_menu()
                        else:
                            print("Opção invalida!\ntente novamente\n")
                            continue
                    
def buscar_livro_nome():
    nome_do_livro_pesquisa = input("Qual o nome do livro ?\n")
    cursor.execute(f"SELECT id_livros, livro, preco, inativo FROM livros WHERE inativo = false and livro ILIKE '%{nome_do_livro_pesquisa}%' ORDER BY id_livros, id_livros ASC; ")
    if cursor.fetchall()==[]:
         print("livro não encotrado")
         volta_ao_menu()
    else:
        cursor.execute(f"SELECT id_livros, livro, preco, inativo FROM livros WHERE inativo = false and livro ILIKE '%{nome_do_livro_pesquisa}%' ORDER BY id_livros, id_livros ASC; ")
        for linha in cursor.fetchall():
            print(f"{linha[0]}) {linha[1]} custa atualmente {linha[2]},")
        volta_ao_menu()
        
def menu():
    escolha_o_menu = input("Escolha uma opção do menu\n1 - Ver lista de livros\n2 - Comprar livros\n3 - Cadastrar novo livro\n4 - Alterar preço de livros\n5 - Ler resumo sobre o livro\n6 - inativar/ativar livro\n7 - Busca de livro por nome\n0 - Fechar sistema\n")
    if escolha_o_menu == '1':
        busca_de_livros()
        volta_ao_menu()
    elif escolha_o_menu == '2':
        comprar_livros()
    elif escolha_o_menu == '3':
        incluir_novos_livros()
    elif escolha_o_menu == '4':
        altera_preco_livro()
    elif escolha_o_menu == '5':
        ler_descricao()
    elif escolha_o_menu == '6':
        inativa_livro()
    elif escolha_o_menu == '7':
        buscar_livro_nome()
    elif escolha_o_menu == '0':
        exit()
    else:
        print("opção invalida!\n")
        volta_ao_menu()
menu()