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
    cursor.execute("SELECT id_livros , livro ,preco FROM public.livros")
    for linha in cursor.fetchall():
        print(f" {linha[0]}) {linha[1]} preço: {linha[2]},")

def incluir_novos_livros():
    while True:
        nome_do_novo_livro =input ("Qual e o nome do livro novo?\n")
        if len(nome_do_novo_livro) >= 5:
            while True:
                nome_do_novo_autor = input("Qual o nome do autor?\n")
                if len(nome_do_novo_autor) >= 10:
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
                elif len(nome_do_novo_autor) <15:
                    print("O nome do autor deve conter no minimo 10 caracters\n")
                    continue
                    
        else:
            print("O nome do livro deve conter no minimo 5 caracters\n")
            continue
            
def menu():
    escolha_o_menu = input("Escolha uma opção do menu\n1- Ver lista de livros\n2- Comprar livros\n3- Cadastrar novo livro\n4- Alterar preço de livros\n5- Ler resumo sobre o livro\n6- inativar algun livro\n")
    if escolha_o_menu == '1':
        busca_de_livros()
        volta_ao_menu()
    elif escolha_o_menu == '2':
        comprar_livros()
    elif escolha_o_menu == '3':
        incluir_novos_livros()
menu()