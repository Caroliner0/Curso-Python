-- Acesso ao banco de dados POSTGRESQL
-- SQL SHELL -> informar a senha do banco
-- Senha local -> coti


-- Remover uma base dados
DROP DATABASE aulap;

-- Criação da base de dados
CREATE DATABASE aulap;

-- Conectar a base de dados
\c aulap

-- Criação da tabela do projeto
-- Produto-> codigo, nome, preco, quantidade

CREATE TABLE produto(
codigo      serial          primary key,
nome        varchar(50)     not null,
preco       decimal         not null
quantidade  integer         not null
);


-- Exibir os objetos do banco de dados
\da

--Descrever o objeto do banco de dados
\d produto

-- Inserir dados na tabela
-- INSERT INTO produto;

INSERT INTO produto (nome, preco quantidade) VALUES ('Mouse', 120.0, 10);

INSERT INTO produto (nome, preco quantidade) VALUES ('Monitor 15 LCD', 400.0, 8);
INSERT INTO produto (nome, preco quantidade) VALUES ('Teclado Microsoft', 50.0, 4;
INSERT INTO produto (nome, preco quantidade) VALUES ('Playstation 5', 8000.0, 7);
INSERT INTO produto (nome, preco quantidade) VALUES ('Xbox One', 800.0, 3);
INSERT INTO produto (nome, preco quantidade) VALUES ('Super Nintendo', 550.0, 9);
INSERT INTO produto (nome, preco quantidade) VALUES ('Master System', 400.0, 10);

SELECT codigo, nome From produto;

SELEC

DELETE FROM produto WHERE codigo = 7;