import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker('pt_PT')
random.seed(42)
np.random.seed(42)

# 1. DADOS GEOGRÁFICOS (Lojas)
print("Gerando dados geográficos...")
lojas = [
    {"loja_id": 1, "nome": "TechSolutions Online", "cidade": "Online", "distrito": "Online", "regiao": "Online", "tipo": "Online"},
    {"loja_id": 2, "nome": "TechSolutions Porto Centro", "cidade": "Porto", "distrito": "Porto", "regiao": "Norte", "tipo": "Física"},
    {"loja_id": 3, "nome": "TechSolutions Porto NorteShopping", "cidade": "Porto", "distrito": "Porto", "regiao": "Norte", "tipo": "Física"},
    {"loja_id": 4, "nome": "TechSolutions Porto Boavista", "cidade": "Porto", "distrito": "Porto", "regiao": "Norte", "tipo": "Física"},
    {"loja_id": 5, "nome": "TechSolutions Lisboa Amoreiras", "cidade": "Lisboa", "distrito": "Lisboa", "regiao": "Lisboa", "tipo": "Física"},
    {"loja_id": 6, "nome": "TechSolutions Lisboa Colombo", "cidade": "Lisboa", "distrito": "Lisboa", "regiao": "Lisboa", "tipo": "Física"},
    {"loja_id": 7, "nome": "TechSolutions Lisboa Vasco da Gama", "cidade": "Lisboa", "distrito": "Lisboa", "regiao": "Lisboa", "tipo": "Física"},
    {"loja_id": 8, "nome": "TechSolutions Braga", "cidade": "Braga", "distrito": "Braga", "regiao": "Norte", "tipo": "Física"},
    {"loja_id": 9, "nome": "TechSolutions Coimbra", "cidade": "Coimbra", "distrito": "Coimbra", "regiao": "Centro", "tipo": "Física"},
    {"loja_id": 10, "nome": "TechSolutions Aveiro", "cidade": "Aveiro", "distrito": "Aveiro", "regiao": "Centro", "tipo": "Física"},
    {"loja_id": 11, "nome": "TechSolutions Faro", "cidade": "Faro", "distrito": "Faro", "regiao": "Algarve", "tipo": "Física"},
    {"loja_id": 12, "nome": "TechSolutions Setúbal", "cidade": "Setúbal", "distrito": "Setúbal", "regiao": "Lisboa", "tipo": "Física"},
    {"loja_id": 13, "nome": "TechSolutions Leiria", "cidade": "Leiria", "distrito": "Leiria", "regiao": "Centro", "tipo": "Física"},
    {"loja_id": 14, "nome": "TechSolutions Viseu", "cidade": "Viseu", "distrito": "Viseu", "regiao": "Centro", "tipo": "Física"},
    {"loja_id": 15, "nome": "TechSolutions Évora", "cidade": "Évora", "distrito": "Évora", "regiao": "Alentejo", "tipo": "Física"},
    {"loja_id": 16, "nome": "TechSolutions Guimarães", "cidade": "Guimarães", "distrito": "Braga", "regiao": "Norte", "tipo": "Física"},
    {"loja_id": 17, "nome": "TechSolutions Funchal", "cidade": "Funchal", "distrito": "Madeira", "regiao": "Madeira", "tipo": "Física"},
    {"loja_id": 18, "nome": "TechSolutions Ponta Delgada", "cidade": "Ponta Delgada", "distrito": "Açores", "regiao": "Açores", "tipo": "Física"},
    {"loja_id": 19, "nome": "TechSolutions Portimão", "cidade": "Portimão", "distrito": "Faro", "regiao": "Algarve", "tipo": "Física"},
    {"loja_id": 20, "nome": "TechSolutions Vila Real", "cidade": "Vila Real", "distrito": "Vila Real", "regiao": "Norte", "tipo": "Física"},
    {"loja_id": 21, "nome": "TechSolutions Santarém", "cidade": "Santarém", "distrito": "Santarém", "regiao": "Centro", "tipo": "Física"},
]

df_lojas = pd.DataFrame(lojas)
df_lojas.to_csv('lojas.csv', index=False, encoding='utf-8-sig')

# 2. CATÁLOGO DE PRODUTOS
print("Gerando catálogo de produtos...")
categorias = {
    "Computadores": ["Portátil", "Desktop", "All-in-One", "Mini PC"],
    "Smartphones": ["Android", "iOS"],
    "Tablets": ["Android", "iOS"],
    "Periféricos": ["Rato", "Teclado", "Monitor", "Webcam", "Headset"],
    "Acessórios": ["Capa", "Película", "Carregador", "Cabo", "Hub USB"],
    "Gaming": ["Consola", "Controller", "Headset Gaming", "Cadeira Gaming"],
    "Audio": ["Auriculares", "Colunas", "Soundbar", "Earbuds"],
    "Smart Home": ["Smart Speaker", "Smart Display", "Smart Plug", "Smart Bulb"],
    "Storage": ["SSD", "HDD", "Pen USB", "Cartão SD"],
    "Networking": ["Router", "Mesh WiFi", "Switch", "Powerline"]
}

produtos = []
produto_id = 1
marcas = ["Apple", "Samsung", "HP", "Dell", "Lenovo", "Asus", "Acer", "Microsoft",
          "Sony", "LG", "Xiaomi", "Logitech", "Razer", "Kingston", "SanDisk"]

for categoria, subcategorias in categorias.items():
    produtos_por_cat = random.randint(18, 23) if categoria in ["Computadores", "Smartphones"] else 9
    for _ in range(produtos_por_cat):
        marca = random.choice(marcas)
        subcategoria = random.choice(subcategorias)

        # Apple só pode ter iOS em Smartphones e Tablets
        # if marca == "Apple":
        #     if categoria == "Smartphones":
        #         subcategoria = "iOS"
        #     elif categoria == "Tablets":
        #         subcategoria = "iOS"
        if categoria in ["Smartphones", "Tablets"]:
            if marca == "Apple":
              subcategoria = "iOS"
            else:
              subcategoria = "Android"

        # Preços base por categoria
        preco_base = {
            "Computadores": (599, 2499), "Smartphones": (199, 1499),
            "Tablets": (249, 1299), "Periféricos": (19, 499),
            "Acessórios": (9, 99), "Gaming": (299, 599),
            "Audio": (29, 399), "Smart Home": (39, 299),
            "Storage": (29, 499), "Networking": (49, 399)
        }

        preco_venda = round(random.uniform(*preco_base[categoria]), 2)
        margem = random.uniform(0.15, 0.35)
        custo = round(preco_venda * (1 - margem), 2)

        produtos.append({
            "produto_id": produto_id,
            "nome": f"{marca} {subcategoria} {random.choice(['Pro', 'Plus', 'Ultra', 'Max', 'Lite', ''])} {random.randint(10, 26)}",
            "categoria": categoria,
            "subcategoria": subcategoria,
            "marca": marca,
            "preco_venda": preco_venda,
            "custo": custo,
            "margem_percentual": round(margem * 100, 2),
            "stock_inicial": random.randint(10, 90)
        })
        produto_id += 1

df_produtos = pd.DataFrame(produtos)
df_produtos.to_csv('produtos.csv', index=False, encoding='utf-8-sig')

# 3. CLIENTES (gerar sem data_registo primeiro)
print("Gerando dados de clientes...")
clientes = []
n_clientes = random.randint(1456, 1588)
for i in range(1, n_clientes):
    genero = random.choice(['M', 'F'])
    idade = random.randint(18, 75)
    # Data de nascimento baseada na idade
    ano_nascimento = 2025 - idade
    data_nascimento = datetime(ano_nascimento, random.randint(1, 12), random.randint(1, 28))
    # Data de registo será ajustada após primeira compra
    clientes.append({
        "cliente_id": i,
        "nome": fake.name_male() if genero == 'M' else fake.name_female(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "data_registo": None,  # Será preenchida depois
        "loja_id": random.choice(df_lojas['loja_id'].unique()),
        "idade": idade,
        "genero": genero,
        "data_nascimento": data_nascimento
    })

df_clientes = pd.DataFrame(clientes)

# 4. HISTÓRICO DE VENDAS (1+ milhões de linhas)
print("Gerando histórico de vendas (isto vai demorar alguns minutos)...")

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 10, 31)
total_days = (end_date - start_date).days

vendas = []
venda_id = 1

# Dicionário para rastrear primeira compra de cada cliente
primeira_compra_cliente = {}

# Pesos para distribuição de vendas por loja (online tem mais volume)
loja_weights = [0.25] + [0.75/20]*20  # 25% online, resto distribuído

# Sazonalidade: Black Friday, Natal, Verão
def fator_sazonalidade(data):
    mes = data.month
    dia = data.day

    # Natal (Dezembro)
    if mes == 12:
        return 1.8
    # Black Friday (final de Novembro)
    elif mes == 11 and dia >= 20:
        return 2.0
    # Verão (Julho-Agosto)
    elif mes in [7, 8]:
        return 1.3
    # Janeiro (Saldos)
    elif mes == 1:
        return 1.4
    else:
        return 1.0

# Tendência de crescimento anual
def fator_crescimento(ano):
    return 1 + (ano - 2020) * random.uniform(0.10, 0.20) # crescimento anual entre 10% a 20%

# Gerar vendas em batches
batch_size = random.randint(50000, 90000)
current_batch = []
header_written = False

for day in range(total_days):
    data_venda = start_date + timedelta(days=day)

    # Número de vendas por dia (variável)
    vendas_dia = int(random.uniform(50, 400) *
                     fator_sazonalidade(data_venda) *
                     fator_crescimento(data_venda.year))

    for _ in range(vendas_dia):
        loja_id = random.choices(df_lojas['loja_id'].tolist(), weights=loja_weights)[0]
        cliente_id = random.randint(1, n_clientes)

        # Rastrear primeira compra
        if cliente_id not in primeira_compra_cliente:
            primeira_compra_cliente[cliente_id] = data_venda

        # Número de produtos por venda (1-5, maioria 1-2)
        num_produtos = random.choices([1, 2, 3, 4, 5], weights=[0.5, 0.3, 0.15, 0.04, 0.01])[0]

        for _ in range(num_produtos):
            produto = df_produtos.sample(1).iloc[0]
            quantidade = random.choices([1, 2, 3], weights=[0.85, 0.12, 0.03])[0]

            # Desconto ocasional
            desconto_perc = random.choices([0, 5, 10, 15, 20], weights=[0.7, 0.15, 0.1, 0.03, 0.02])[0]
            preco_unitario = produto['preco_venda'] * (1 - desconto_perc/100)

            current_batch.append({
                "venda_id": venda_id,
                "data_venda": data_venda.strftime('%Y-%m-%d'),
                "loja_id": loja_id,
                "cliente_id": cliente_id,
                "produto_id": produto['produto_id'],
                "quantidade": quantidade,
                "preco_unitario": round(preco_unitario, 2),
                "desconto_percentual": desconto_perc,
                "custo_unitario": produto['custo'],
                "valor_total": round(preco_unitario * quantidade, 2)
            })
            venda_id += 1

    # Salvar batch quando atingir o tamanho
    if len(current_batch) >= batch_size:
        df_batch = pd.DataFrame(current_batch)
        mode = 'w' if not header_written else 'a'
        header = not header_written
        df_batch.to_csv('vendas.csv', mode=mode, header=header, index=False, encoding='utf-8-sig')
        header_written = True
        current_batch = []
        print(f"  Processadas {venda_id:,} vendas...")

# Salvar últimas vendas
if current_batch:
    df_batch = pd.DataFrame(current_batch)
    mode = 'w' if not header_written else 'a'
    header = not header_written
    df_batch.to_csv('vendas.csv', mode=mode, header=header, index=False, encoding='utf-8-sig')

# Atualizar data de registo dos clientes baseada na primeira compra
print("Atualizando datas de registo dos clientes...")
for idx, row in df_clientes.iterrows():
    cliente_id = row['cliente_id']
    if cliente_id in primeira_compra_cliente:
        primeira_compra = primeira_compra_cliente[cliente_id]
        # Data de registo entre 0-365 dias antes da primeira compra
        dias_antes = random.randint(0, 365)
        data_registo = primeira_compra - timedelta(days=dias_antes)
        # Garantir que data de registo não é antes de o cliente ter 18 anos
        data_minima_registo = row['data_nascimento'] + timedelta(days=365*18)
        if data_registo < data_minima_registo:
            data_registo = data_minima_registo
        df_clientes.at[idx, 'data_registo'] = data_registo.strftime('%Y-%m-%d')
    else:
        # Cliente sem compras - data de registo aleatória após 18 anos
        data_minima_registo = row['data_nascimento'] + timedelta(days=365*18)
        data_registo = fake.date_between(start_date=data_minima_registo.date(), end_date='today')
        df_clientes.at[idx, 'data_registo'] = data_registo

# Remover coluna auxiliar e salvar clientes
df_clientes = df_clientes.drop('data_nascimento', axis=1)
df_clientes.to_csv('clientes.csv', index=False, encoding='utf-8-sig')

print(f"\n✓ Ficheiros gerados com sucesso!")
print(f"  - lojas.csv: {len(df_lojas)} lojas")
print(f"  - produtos.csv: {len(df_produtos)} produtos")
print(f"  - clientes.csv: {len(df_clientes)} clientes")
print(f"  - vendas.csv: {venda_id:,} transações")
print(f"\nTotal estimado de linhas de vendas: {venda_id:,}")
print(f"Período: 2020-01-01 a 2025-10-31")