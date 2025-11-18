# sales-dashbaord

1. Os dados foram gerados através de uma script em python localizada em /data/
2. Data Warehousing

DIM_DATA(data_id, data, ano, trimestre, mês, dia_semana)
DIM_LOJA(loja_id, nome, cidade, distrito, região, tipo)
DIM_CLIENTE(cliente_id, genero, loja_id, faixa_etaria, data_registo), DIM_PRODUTO(produto_id, nome, categoria, subcategoria, marca, margem_percentual, preco_venda, custo)
FACT_VENDAS(venda_id, data_id, loja_id, cliente_id, produto_id, quantidade, preco_unitario, desconto_pct, custo_unitario, valor_total)
