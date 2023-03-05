import numpy as np 
import pandas as pd 
import psycopg2

conexao = psycopg2.connect(host='localhost', 
                        database='Biblioteca',
                        user='postgres', 
                        password='postgres')
cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies\
    (\
        idmovies bigserial primary key,\
        Title varchar(100) NOT NULL,\
        Rating numeric(3,2) NOT NULL,\
        Year integer NOT NULL,\
        Month varchar(10) NOT NULL,\
        Certificate varchar(20) NOT NULL,\
        Runtime integer NOT NULL,\
        Directors varchar(200) NOT NULL,\
        stars varchar(2000) NOT NULL,\
        Genre varchar(60) NOT NULL,\
        Filming_location varchar(300) NOT NULL,\
        Budget varchar(30) NOT NULL,\
        Income varchar NOT NULL,\
        Country_of_origin varchar(100) NOT NULL\
    )")

conexao.commit()

planilha = pd.read_csv("D:\movies.csv")



indice = 0
for indice in range(len(planilha)):

    title=planilha.loc[indice,"Title"]
    title_rep = title.replace("'","''")
    rating=planilha.loc[indice,"Rating"]
    rating_rep = str(rating).replace("'","''")
    year=planilha.loc[indice,"Year"]
    year_rep = str(year).replace("'","''")
    month=planilha.loc[indice,"Month"]
    month_rep=month.replace("'","''")
    certificate=planilha.loc[indice,"Certificate"]
    certificate_rep=str(certificate).replace("'","''")
    runtime=planilha.loc[indice,"Runtime"]
    runtime_rep=str(runtime).replace("Unknown","0").replace("'","''")
    directors=planilha.loc[indice,"Directors"]
    directors_rep=directors.replace("'","''")
    stars=planilha.loc[indice,"Stars"]
    stars_rep=stars.replace("'","''")
    genre=planilha.loc[indice,"Genre"]
    genre_rep=genre.replace("'","''")
    filming_location=planilha.loc[indice,"Filming_location"]
    filming_location_rep = filming_location.replace("'","''")
    budget=planilha.loc[indice,"Budget"]
    budget_rep=str(budget).replace("'","''")
    income=planilha.loc[indice,"Income"]
    income_rep = str(income).replace("'","''")
    country_of_origin=planilha.loc[indice,"Country_of_origin"]
    country_of_origin_rep = country_of_origin.replace("'","''")
    print(planilha.loc[indice])
    cursor.execute(f"INSERT INTO movies\
    (title, rating, year, month, certificate, runtime, directors, stars, genre, filming_location, budget, income, country_of_origin)\
    VALUES ('{title_rep}','{rating_rep}','{year_rep}','{month_rep}','{certificate_rep}','{runtime_rep}','{directors_rep}','{stars_rep}','{genre_rep}','{filming_location_rep}','{budget_rep}','{income_rep}','{country_of_origin_rep}');"
    )
    conexao.commit()

    
     
    



        