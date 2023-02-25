import pandas as pd
import matplotlib.pyplot as plt

# importando arquivo xls e filtrando colunas mais relevantes
planilha = pd.read_excel("D:/UFs_IBGE.xls",\
    usecols =["UF [-]","Área Territorial - km² [2021]","População estimada - pessoas [2021]",\
                    "Densidade demográfica - hab/km² [2010]"])

# calculando densidade demográfica de 2021
densidade_demografica_2021 = planilha["População estimada - pessoas [2021]"] / planilha["Área Territorial - km² [2021]"]


# calculando aumento da densidade demográfica deste 2010 ate 2021
aumento_desidade_democrafica = densidade_demografica_2021 - planilha[ "Densidade demográfica - hab/km² [2010]"]

# adicionando as novas colunas ao dataframe
planilha["Densidade demográfica - hab/km² [2021]"] = densidade_demografica_2021
planilha["Aumento na densidade demográfica"] = aumento_desidade_democrafica

# plotando o grafico com as informações adiquiridas
plt.figure(figsize=(12,6))
plt.bar(x=planilha["UF [-]"],height=planilha["Densidade demográfica - hab/km² [2021]"],color = "green",label = "Densidade demográfica - hab/km² - 2021")
plt.bar(x=planilha["UF [-]"],height=planilha["Densidade demográfica - hab/km² [2010]"],color = "blue",alpha=0.5 , label = "Densidade demográfica - hab/km² - 2010")
plt.bar(x=planilha["UF [-]"],height=planilha["Aumento na densidade demográfica"],color = "yellow",label = "Aumento da densidade domografica de 2010 até 2021")
plt.xticks(rotation=90)
plt.legend(loc="best")
plt.show()





