USE [SalesDW];
GO
SET LANGUAGE Portuguese;
SET NOCOUNT ON;
GO

CREATE OR ALTER VIEW dw.vw_cliente_loja AS
SELECT
    c.cliente_id,
    c.genero,
    c.loja_id,
    c.faixa_etaria,
    c.data_registo,
    l.nome   AS loja_nome,
    l.cidade,
    l.distrito,
    l.regiao,
    l.tipo
FROM dw.DIM_CLIENTE AS c
LEFT JOIN dw.DIM_LOJA AS l
    ON l.loja_id = c.loja_id;
GO
