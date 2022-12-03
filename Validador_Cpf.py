import re  
cpf_digitado = re.sub(r'[^0-9]','',input("digite seu cpf\n"))
quantidade_digitos_cpf = len(cpf_digitado)
entrada_sequecial = cpf_digitado == cpf_digitado[0] * quantidade_digitos_cpf

if entrada_sequecial == True:
    print("cpf invalido!")
    exit()

if quantidade_digitos_cpf >= 11:
    digito_cpf_1 = int(cpf_digitado[0]) * 10
    digito_cpf_2 = int(cpf_digitado[1]) * 9
    digito_cpf_3 = int(cpf_digitado[2]) * 8 
    digito_cpf_4 = int(cpf_digitado[3]) * 7 
    digito_cpf_5 = int(cpf_digitado[4]) * 6
    digito_cpf_6 = int(cpf_digitado[5]) * 5
    digito_cpf_7 = int(cpf_digitado[6]) * 4
    digito_cpf_8 = int(cpf_digitado[7]) * 3
    digito_cpf_9 = int(cpf_digitado[8]) * 2
    
    soma_dos_9digitos = digito_cpf_1 + digito_cpf_2 + digito_cpf_3 + digito_cpf_4 + digito_cpf_5 \
                        + digito_cpf_6 + digito_cpf_7 + digito_cpf_8 + digito_cpf_9
    descimo_digito = (soma_dos_9digitos * 10) % 11 
    novo_digito = descimo_digito if descimo_digito <= 9  else  0
    
    digito_cpf_1 = int(cpf_digitado[0]) * 11
    digito_cpf_2 = int(cpf_digitado[1]) * 10
    digito_cpf_3 = int(cpf_digitado[2]) * 9 
    digito_cpf_4 = int(cpf_digitado[3]) * 8 
    digito_cpf_5 = int(cpf_digitado[4]) * 7
    digito_cpf_6 = int(cpf_digitado[5]) * 6
    digito_cpf_7 = int(cpf_digitado[6]) * 5
    digito_cpf_8 = int(cpf_digitado[7]) * 4
    digito_cpf_9 = int(cpf_digitado[8]) * 3
    digito_cpf_10 = novo_digito * 2
    
    soma_dos_10digitos = digito_cpf_1 + digito_cpf_2 + digito_cpf_3 + digito_cpf_4 + digito_cpf_5 \
                        + digito_cpf_6 + digito_cpf_7 + digito_cpf_8 + digito_cpf_9 + digito_cpf_10
    descimo_primeiro_digito = (soma_dos_10digitos * 10) % 11 
    novo_digito2 = descimo_primeiro_digito if descimo_primeiro_digito <= 9  else  0
    novo_digito_str = str(novo_digito)
    novo_digito2_str = str(novo_digito2)
    DIGITOS_DE_CPF = cpf_digitado[0] + cpf_digitado[1] + cpf_digitado[2] + cpf_digitado[3] \
                    + cpf_digitado[4] + cpf_digitado[5] + cpf_digitado[6] + cpf_digitado[7] \
                        + cpf_digitado[8] + novo_digito_str + novo_digito2_str
    if DIGITOS_DE_CPF == cpf_digitado:  
        print(f"O cpf { DIGITOS_DE_CPF} e valido")
    else: 
        print(f"O cpf {DIGITOS_DE_CPF} não e valido!")
else:
    print("Quantidade de caracteres e invalida, digite 11 caracteres")
    