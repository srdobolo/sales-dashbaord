# Visual Calculations

## Pareto

```dax
Percent of grand total = DIVIDE([Vendas Totais], COLLAPSEALL([Vendas Totais], ROWS))
```

```dax
Running sum = RUNNINGSUM([Percent of grand total],ORDERBY([Vendas Totais],DESC))
```

```dax
Greenline = IF([Pareto]<=.8,[Pareto],BLANK())
```

```dax
Redline = IF([Pareto]>.8,[Pareto],BLANK())
```

https://www.youtube.com/watch?v=xhc8WNoeyos

## Cross Selling Matrix

### Criar Tabela Comparação

```dax
Comparação Produtos = 
SUMMARIZE('dw DIM_PRODUTO','dw DIM_PRODUTO'[produto_id],'dw DIM_PRODUTO'[nome])
```

### Medida

```dax
Purchased Both Products = 
VAR InitialPurchase = VALUES('dw DIM_CLIENTE'[cliente_id])
VAR ComparisonPurchase = CALCULATETABLE(VALUES('dw DIM_CLIENTE'[cliente_id]), ALL('dw DIM_PRODUTO'),
TREATAS(VALUES('Comparison Products'[Index]),'dw FACT_VENDAS'[produto_id]))
RETURN
IF(SELECTEDVALUE('dw DIM_PRODUTO'[nome]) = SELECTEDVALUE('Comparison Products'[Comparison Product]),
BLANK(),
COUNTROWS(INTERSECT(InitialPurchase,ComparisonPurchase)))
```


## Cohort

https://www.youtube.com/watch?v=vbg4Je1tuis