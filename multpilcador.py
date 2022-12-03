valores_para_multplicação = input("Digite o numero para multplicação\n")
valores_para_multplicação_int =int(valores_para_multplicação)
def multiplicacao_de_valores():
    continuar_iserir_valores = True
    while continuar_iserir_valores:
        novo_valor_para_multplica = input("Digite o novo numero para multplicação\n")
        novo_valor_para_multplicas_int = int(novo_valor_para_multplica)
        opcao_entrada_volares = input("Deseja incluir novos valores para multplicação?\n [S]im ou [N]ão\n").upper()
        if opcao_entrada_volares == "N":
            resultado_multplicação = valores_para_multplicação_int * novo_valor_para_multplicas_int
            print(f" o valor digitado é {resultado_multplicação}")
            
multiplicacao_de_valores()