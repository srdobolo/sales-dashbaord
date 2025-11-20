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
