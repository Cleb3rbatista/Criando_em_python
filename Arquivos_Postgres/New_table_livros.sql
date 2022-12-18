CREATE TABLE livros 
(
	id_livros bigserial PRIMARY KEY,
    livro VARCHAR(100) NOT NULL,
    autor VARCHAR (50) NOT NULL,
    sexo_do_autor CHAR(1) NOT NULL,
    ano_de_lancamento NUMERIC(4,0),
    descricao VARCHAR(2000),
    preco money,
    inativo BOOLEAN NOT NULL default FALSE
)
