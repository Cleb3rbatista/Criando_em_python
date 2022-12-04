questionarios = [
    {
        "Pergunta" : "Quanto é 5x5?" ,
        "Opções" : ['27', '13', '25', '121'] ,
        "Resposta" : "25",
    },
    {
        "Pergunta" : "Qual e a raiz cubica de 125?",
        "Opções" : ['4', '5','2','3'],
        "Resposta" : "5",
    },
    {
        "Pergunta" : "Qual e o resultado de 214/2?",
        "Opções": ['106', '121', '107', '99'],
        "Resposta" : "107"
    },
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0
for pergunta in questionarios:
    print( 'pergunta', pergunta['Pergunta'])
    print()

    alternativas = pergunta['Opções']
    for i ,opcao in enumerate(alternativas):
        print(f'{i})',opcao)
    print()
    
    escolha = input("Escolha uma opção\n ")
    
    acertou = False
    escolha_int = None
    qtd_escolhas = len(pergunta['Opções'] )
    
    if escolha.isdigit():
        escolha_int = int(escolha) 
    
    if escolha_int is not None:
        if escolha_int >=1 and escolha_int <= qtd_escolhas:
            if alternativas[escolha_int] == pergunta['Resposta']:
                acertou = True
      
    print()           
    if acertou == True:
        qtd_acertos+=1   
        print("voce acertou")
    else:
        print("voce errou")
print()

print("Voce acertou", qtd_acertos)
print("de", len(questionarios), "perguntas")