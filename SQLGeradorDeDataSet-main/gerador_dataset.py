import pandas as pd
import random
from faker import Faker
from datetime import timedelta
from datetime import date

# Instância do Faker
fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

# Lista de IDs de produtos a serem excluídos das vendas
produtos_excluidos = {4, 7, 9, 14, 34}

# IDs de produtos que não estão na tabela de produtos
produtos_fora_catalogo = [80, 123, 444]

# Gerar tabela de vendas com sazonalidade e distribuição não uniforme
def gerar_tabela_vendas():
    vendas = []
    inicio = pd.Timestamp('2013-01-01')
    fim = pd.Timestamp('2023-12-31')

    # Produtos populares (1 a 10)
    produtos_populares = list(range(1, 11))

    # Loop por cada mês nos últimos 10 anos
    data_atual = inicio
    while data_atual <= fim:
        mes = data_atual.month

        # Definir o número de vendas com sazonalidade
        if mes == 11:  # Black Friday
            num_vendas = random.randint(2000, 3000)
        elif mes == 2:  # Volta às aulas / Carnaval
            num_vendas = random.randint(1500, 2500)
        else:
            num_vendas = random.randint(1000, 1500)

        # Gerar vendas para o mês atual
        for _ in range(num_vendas):
            # Selecionar produtos do catálogo ou fora dele
            if random.random() < 0.95:  # 95% de chance de escolher produtos do catálogo
                id_produto = random.choices(
                    population=range(1, 51),  # Todos os produtos
                    weights=[5 if p in produtos_populares else 1 for p in range(1, 51)],
                    k=1
                )[0]
                # Excluir produtos com IDs indesejados
                if id_produto in produtos_excluidos:
                    continue
            else:  # 5% de chance de escolher produtos fora do catálogo
                id_produto = random.choice(produtos_fora_catalogo)

            # Gerar data de venda entre a data atual e a data final (fim)
            data_venda = fake.date_between(start_date=data_atual, end_date=fim)

            vendas.append({
                'id_venda': len(vendas) + 1,
                'id_cliente': random.randint(1, 500),  # 500 clientes únicos
                'id_produto': id_produto,
                'quantidade': random.randint(1, 5),
                'data_venda': data_venda
            })

        # Avançar para o próximo mês
        data_atual += pd.DateOffset(months=1)
    
    return pd.DataFrame(vendas)

# Gerar tabela de clientes com nomes separados
def gerar_tabela_clientes():
    clientes = []
    for i in range(1, 501):  # 500 clientes únicos
        nome_completo = fake.name()
        partes = nome_completo.split()
        primeiro_nome = partes[0]
        ultimo_nome = partes[-1]
        segundo_nome = " ".join(partes[1:-1]) if len(partes) > 2 else None
        clientes.append({
            'id_cliente': i,
            'primeiro_nome': primeiro_nome,
            'segundo_nome': segundo_nome,
            'ultimo_nome': ultimo_nome,
            'cidade': fake.city(),
            'idade': random.randint(18, 65),
            'data_cadastro': fake.date_between(start_date=date(2012, 1, 1), end_date=date(2023, 1, 1))
        })
    return pd.DataFrame(clientes)

# Gerar tabela de produtos com preços condizentes
def gerar_tabela_produtos():
    produtos = []
    categorias = {
        'Eletrônicos': (500, 2000),
        'Móveis': (200, 1000),
        'Roupas': (50, 300),
        'Beleza': (20, 150),
        'Alimentos': (10, 100)
    }

    for i in range(1, 51):  # 50 produtos únicos
        categoria = random.choice(list(categorias.keys()))
        preco_min, preco_max = categorias[categoria]
        produtos.append({
            'id_produto': i,
            'nome_produto': fake.word().capitalize(),
            'categoria': categoria,
            'preco_unitario': round(random.uniform(preco_min, preco_max), 2)
        })
    return pd.DataFrame(produtos)

# Gerando as tabelas
tabela_vendas = gerar_tabela_vendas()  # Gerando a tabela de vendas
tabela_clientes = gerar_tabela_clientes()  # Gerando a tabela de clientes
tabela_produtos = gerar_tabela_produtos()  # Gerando a tabela de produtos

# Convertendo a coluna 'data_venda' para datetime
tabela_vendas['data_venda'] = pd.to_datetime(tabela_vendas['data_venda'])

# Análise de Vendas por Mês
tabela_vendas['ano_mes'] = tabela_vendas['data_venda'].dt.to_period('M')
tabela_vendas_com_preco = tabela_vendas.merge(tabela_produtos[['id_produto', 'preco_unitario']], on='id_produto')
tabela_vendas_com_preco['receita'] = tabela_vendas_com_preco['quantidade'] * tabela_vendas_com_preco['preco_unitario']
vendas_por_mes = tabela_vendas_com_preco.groupby('ano_mes').agg(
    total_vendas=('quantidade', 'sum'),
    total_receita=('receita', 'sum')
).reset_index()

# Produtos Não Vendidos
todos_produtos = tabela_produtos['id_produto'].unique()
produtos_vendidos = tabela_vendas['id_produto'].unique()
produtos_nao_vendidos = set(todos_produtos) - set(produtos_vendidos)
produtos_nao_vendidos_info = tabela_produtos[tabela_produtos['id_produto'].isin(produtos_nao_vendidos)]

# Exibindo resultados
print("\nProdutos Não Vendidos:")
print(produtos_nao_vendidos_info)

print("\nVendas por Mês:")
print(vendas_por_mes.head(10))

print("\nTabela de Vendas:")
print(tabela_vendas.head())

print("\nTabela de Clientes:")
print(tabela_clientes.head())

print("\nTabela de Produtos:")
print(tabela_produtos.head())

# Salvando as tabelas em arquivos CSV
tabela_vendas.to_csv('tabela_vendas.csv', index=False)
tabela_clientes.to_csv('tabela_clientes.csv', index=False)
tabela_produtos.to_csv('tabela_produtos.csv', index=False)
