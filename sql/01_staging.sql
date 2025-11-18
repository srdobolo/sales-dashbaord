USE [SalesDW];
GO

/* Atualiza staging a partir do OLTP SalesDB */
DROP TABLE IF EXISTS staging.lojas;
SELECT * INTO staging.lojas FROM SalesDB.dbo.lojas;

DROP TABLE IF EXISTS staging.clientes;
SELECT * INTO staging.clientes FROM SalesDB.dbo.clientes;

DROP TABLE IF EXISTS staging.produtos;
SELECT * INTO staging.produtos FROM SalesDB.dbo.produtos;

DROP TABLE IF EXISTS staging.vendas;
SELECT * INTO staging.vendas FROM SalesDB.dbo.vendas;

CREATE INDEX IX_staging_vendas_data ON staging.vendas (data_venda);
CREATE INDEX IX_staging_vendas_loja ON staging.vendas (loja_id);
CREATE INDEX IX_staging_vendas_cliente ON staging.vendas (cliente_id);
CREATE INDEX IX_staging_vendas_produto ON staging.vendas (produto_id);
GO
