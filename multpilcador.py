valores_para_multplicação = input("Digite o numero para multplicação\n")
def multiplicacao_de_valores():
    continuar_iserir_valores = True
    while continuar_iserir_valores:
        novo_valor_para_multplica = input("Digite o novo numero para multplicação\n")
        opcao_entrada_volares = input("Deseja incluir novos valores para multplicação?\n [S]im ou [N]ão\n").upper()
        if opcao_entrada_volares == "N":
            resultado_multplicação = valores_para_multplicação * novo_valor_para_multplica
            print(resultado_multplicação)
multiplicacao_de_valores()