import datetime
import time
hoje = datetime.date.today()
anoAtual = hoje.strftime('%Y')  
meses = {'janeiro' : 1, 'fevereiro' : 2, 'março' : 3, 'abril' : 4, 'maio' : 5, 'junho' : 6, 'julho' : 7, 'agosto' : 8, 'setembro' : 9, 'outubro' : 10, 'novembro' : 11, 'dezembro' : 12}
while True:
    try:
        dia = int(input("Digite o dia do seu nascimento\n"))
    except ValueError:
        print("0 valor para Dia deve ser um numero inteiro!")
        continue
    else:
        break
while True:
    try:
        mes = int(input("Digite o mes do seu nascimento\n"))
        if mes < 1 or mes > 12 :
            print("o valor para mes deve estar entre 1 e 12!")
            break
    except ValueError:
        print(" O valor para o  Mes deve ser um numero inteiro!")
        continue
    else:
        break
while True:
    try:
        ano = int(input("Digite o ano do seu nascimento\n"))
    except ValueError:
        print(" digite um valor inteiro!")
        continue
    else:
        break 
while True:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes== 10 or mes ==12:
        if dia > 31:
            print("Esse mês só tem 31 dias")
            break
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print("Esse mês só tem 30 dias")
            break
    if mes == 2:
        for i in range(0 , 3):
            print("Verificando se o ano e bissexto...")
            time.sleep(0.75)
        bissexto = ano % 4 
        if bissexto == 0:
                print(" Ano e bissexto")
                if dia > 29:
                    print(" Esse mes só tem 29 dias")
                    break
        if bissexto != 0 :
            print("esse ano não e bissexto")
            if dia > 28:
                    print("Esse mês so tem 28 dias") 
                    break
    variavel_int = int(anoAtual)
    result = ano - variavel_int
    if result > 0:
            print("Voce nascel no futuro ?")
            break
    else:
        print("Sua data de nascimento e:",dia ,"de", mes, "de", ano ,"\n")  
        niver = datetime.date(ano , mes , dia)
        idade_em_dias = hoje - niver
        print(" sua idade em dias e de:", idade_em_dias.days,".")
        break