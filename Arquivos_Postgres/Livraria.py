import psycopg2
import os
def comprar_livros():
    conexao = psycopg2.connect(host='localhost', 
                        database='Biblioteca',
                        user='postgres', 
                        password='postgres')
    cursor = conexao.cursor()

    cursor.execute("SELECT id_livros , livro ,preco FROM public.livros")

    for linha in cursor.fetchall():
        print(f" {linha[0]}) {linha[1]} preço: {linha[2]},")
    while True:
        deseja_comprar = input("Deseja comprar um livro?\n [S]im ou [N]ão\n").upper()
        if deseja_comprar == "N":
            print("Saindo...")
            exit()
            
        elif deseja_comprar == "S":
            while True:
                try:
                    
                    idlivro_escolhido = int(input("Qual o numero do livro que voce deseja comprar?\n"))
                    cursor.execute(f"SELECT id_livros  FROM public.livros")
                    qtd_livros =len(cursor.fetchall())
                    if idlivro_escolhido > qtd_livros:
                        print(f"Atualmente a somete {qtd_livros} na biblioteca")   
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
            confirmando_livro = input(f"O livro escolhido e {livro_para_comprar[1]}?\n [S]im ou [N]ão\n").upper()
        
            if confirmando_livro == "S":
                print(f"O livro {livro_para_comprar[1]} custa {livro_para_comprar[6]}")
                
            elif confirmando_livro == "N":
                escolher_novamente=input("lamento, deseja escolher novamente?\n [S]im ou [N]ão\n").upper()
                
                if escolher_novamente == "S":
                    os.system("cls")
                    comprar_livros()
                    
                elif escolher_novamente == "N":
                    print("Saindo...")
                    exit()
                    
                else:
                    print("opção invalida!")
            else:
                print("opção invalida!")           


        conexao.close()
        cursor.close()
comprar_livros()