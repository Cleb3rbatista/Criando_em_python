import psycopg2
import os
def comprar_livros():
    conexao = psycopg2.connect(host='localhost', 
                        database='Biblioteca',
                        user='postgres', 
                        password='postgres')
    cursor = conexao.cursor()

    cursor.execute("SELECT id_livro , livro ,preco FROM public.livros")

    for linha in cursor.fetchall():
        print(f"numero de indetificação do livro {linha[0]}, nome do livro {linha[1]}, preço {linha[2]},")
        
    deseja_comprar = input("Deseja comprar um livro?\n [S]im ou [N]ão\n").upper()
    if deseja_comprar == "N":
        exit()
        
    elif deseja_comprar == "S":
        idlivro_escolhido = int(input("Qual o numero do livro que voce deseja comprar?\n"))
        cursor.execute(f"SELECT id_livro  FROM public.livros WHERE id_livro = '{idlivro_escolhido}'")
        if cursor.fetchone==[]:
            print("Livro não encontrado")
            
        cursor.execute(f"SELECT *  FROM public.livros WHERE id_livro = '{idlivro_escolhido}'")
        
        for livro_para_comprar in cursor.fetchall():
            confirmando_livro = input(f"O livro escolhido e {livro_para_comprar[1]}?\n [S]im ou [N]ão\n").upper()
        
            if confirmando_livro == "S":
                print(f"O livro {livro_para_comprar[1]} custa {livro_para_comprar[6]}")
                
            elif confirmando_livro == "N":
                escolher_novamente=input("lamento, deseja escolher novamente?\n [S]im ou [N]ão\n")
                
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
    else:
        print("opção invalida!")



    conexao.close()
    cursor.close()
comprar_livros()