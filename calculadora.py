from ast import Break
def calculadora():
    operacao = input('''escolha a operação matematica que deseja seguir,
selecione + para adição
- para subtrção 
* para multiplcação 
 / para divisao\n''')
    while True:
        try:
            numero_1 = float(input("digite o primeiro numero\n "))
        except ValueError:
            print("digite um numero Real")
            continue
        else:
            break
    while True:
        try:
            numero_2 = float(input("digite o segundo numero\n" ))
        except ValueError:
            print("digite um numero Real")
            continue
        else:
            break
    if operacao == '+':
        print(" {},{} =".format( numero_1, numero_2))
        print( numero_1 + numero_2 )
    elif operacao == '-':
        print(" {},{} =".format( numero_1, numero_2))
        print( numero_1 - numero_2 )
    elif operacao == '*':
        print(" {},{} =".format( numero_1, numero_2))
        print( numero_1 * numero_2 )
    elif operacao == '/': 
        try:
            print(" {},{} =".format( numero_1, numero_2))
            resultdiv = numero_1 // numero_2
            print("O resultado e:", resultdiv)
        except ZeroDivisionError:
            print(" o divisor deve ser um numero diferente de zero")
            else:
                break
    else:
        print("digite um operador valido!")
    calcular_novamente()
def calcular_novamente():
    while True:
        calc_new= input(" deseja usar a calculadora novamente?\n S para sim e N para não\n")
        if calc_new.upper() =='S':
            calculadora()
        elif calc_new.upper()=='N':
            print("Até logo!")
            break
        else:
            print("opção invalida, tente novamente")
            calcular_novamente()
calculadora()
