USE [SalesDW];
GO
SET LANGUAGE Portuguese;
SET NOCOUNT ON;

DROP TABLE IF EXISTS dw.DIM_DATA;
DROP TABLE IF EXISTS dw.DIM_LOJA;
DROP TABLE IF EXISTS dw.DIM_CLIENTE;
DROP TABLE IF EXISTS dw.DIM_PRODUTO;
GO

CREATE TABLE dw.DIM_DATA (
    data_id     INT IDENTITY(1,1) PRIMARY KEY,
    data        DATE        NOT NULL UNIQUE,
    ano         INT         NOT NULL,
    trimestre   CHAR(2)     NOT NULL,
    mes         VARCHAR(15) NOT NULL,
    dia_semana  VARCHAR(15) NOT NULL
);

INSERT INTO dw.DIM_DATA (data, ano, trimestre, mes, dia_semana)
SELECT DISTINCT
       v.data_venda,
       YEAR(v.data_venda),
       CONCAT('T', DATEPART(QUARTER, v.data_venda)),
       DATENAME(MONTH, v.data_venda),
       DATENAME(WEEKDAY, v.data_venda)
FROM staging.vendas AS v;

CREATE TABLE dw.DIM_LOJA (
    loja_id   INT PRIMARY KEY,
    nome      NVARCHAR(150) NOT NULL,
    cidade    NVARCHAR(80)  NOT NULL,
    distrito  NVARCHAR(80)  NOT NULL,
    regiao    NVARCHAR(80)  NOT NULL,
    tipo      NVARCHAR(30)  NOT NULL
);

INSERT INTO dw.DIM_LOJA
SELECT DISTINCT
       loja_id, nome, cidade, distrito, regiao, tipo
FROM staging.lojas;

CREATE TABLE dw.DIM_CLIENTE (
    cliente_id    INT PRIMARY KEY,
    genero        CHAR(1)      NULL,
    loja_id       INT          NULL,
    faixa_etaria  VARCHAR(20)  NOT NULL,
    data_registo  DATE         NULL
);

INSERT INTO dw.DIM_CLIENTE (cliente_id, genero, loja_id, faixa_etaria, data_registo)
SELECT DISTINCT
       c.cliente_id,
        c.genero,
        c.loja_id,
        CASE
            WHEN c.idade < 25 THEN '<25'
            WHEN c.idade BETWEEN 25 AND 34 THEN '25-34'
            WHEN c.idade BETWEEN 35 AND 44 THEN '35-44'
            WHEN c.idade BETWEEN 45 AND 54 THEN '45-54'
            WHEN c.idade BETWEEN 55 AND 64 THEN '55-64'
            ELSE '65+'
        END,
        c.data_registo
FROM staging.clientes AS c;

CREATE TABLE dw.DIM_PRODUTO (
    produto_id        INT PRIMARY KEY,
    nome              NVARCHAR(200) NOT NULL,
    categoria         NVARCHAR(100) NOT NULL,
    subcategoria      NVARCHAR(100) NOT NULL,
    marca             NVARCHAR(80)  NOT NULL,
    margem_percentual DECIMAL(6,2)  NOT NULL,
    preco_venda       DECIMAL(18,2) NOT NULL,
    custo             DECIMAL(18,2) NOT NULL
);

INSERT INTO dw.DIM_PRODUTO
SELECT DISTINCT
       produto_id,
       nome,
       categoria,
       subcategoria,
       marca,
       margem_percentual,
       preco_venda,
       custo
FROM staging.produtos;
GO
