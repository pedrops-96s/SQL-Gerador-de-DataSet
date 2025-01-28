# Gerador de Dataset de Vendas, Clientes e Produtos

Este projeto tem como objetivo gerar datasets sintéticos de vendas, clientes e produtos com base em um cenário fictício. O código utiliza a biblioteca `Faker` para gerar dados realistas e `pandas` para manipulação e análise de dados. Além disso, o código realiza análises simples, como a verificação de produtos não vendidos e a análise de vendas por mês.

## Funcionalidades

1. **Geração de Dados de Vendas**:
   - Gera dados de vendas de produtos de uma loja.
   - Considera sazonalidade nas vendas, como aumento de vendas durante a Black Friday e a temporada de volta às aulas.
   - Gera vendas mensais entre os anos de 2013 a 2023.

2. **Geração de Dados de Clientes**:
   - Cria uma lista de clientes fictícios, com nome, cidade, idade e data de cadastro.

3. **Geração de Dados de Produtos**:
   - Gera produtos com categorias e preços simulados, como Eletrônicos, Móveis, Roupas, Beleza e Alimentos.

4. **Análise de Vendas**:
   - Realiza análise de vendas mensais, incluindo o total de vendas e a receita gerada.
   - Verifica quais produtos não foram vendidos durante o período analisado.

5. **Exportação dos Dados**:
   - Exporta as tabelas de vendas, clientes e produtos para arquivos CSV.

## Pré-requisitos

Antes de rodar o código, é necessário instalar as dependências:

```bash
pip install pandas faker
Como Usar
Clone ou baixe o repositório para o seu computador.

Execute o script Python para gerar os dados e realizar a análise:

bash
Copiar
python gerador_dataset.py
O script irá gerar três arquivos CSV:
tabela_vendas.csv: Contém as informações de vendas geradas.
tabela_clientes.csv: Contém as informações de clientes gerados.
tabela_produtos.csv: Contém as informações de produtos gerados.
Estrutura do Código
Funções:
gerar_tabela_vendas(): Gera a tabela de vendas com base em um período de 10 anos, considerando sazonalidade e produtos excluídos.

gerar_tabela_clientes(): Gera uma tabela de clientes com 500 registros e informações como nome, cidade, idade e data de cadastro.

gerar_tabela_produtos(): Gera uma tabela de 50 produtos com preços e categorias realistas.

Análise de Vendas: Após gerar as tabelas, o código executa:

Análise de vendas por mês (total de vendas e receita por mês).
Identificação de produtos não vendidos durante o período.
Exemplo de Saída:
Ao executar o código, a saída será algo como:

python
Copiar
Produtos Não Vendidos:
   id_produto nome_produto     categoria  preco_unitario
3           4    Produto X    Eletrônicos          1499.0
...
Vendas por Mês:
   ano_mes  total_vendas  total_receita
0  2013-01              120          12000
...
Tabela de Vendas:
   id_venda  id_cliente  id_produto  quantidade data_venda
0         1           12           2           3  2013-01-15
...
Tabela de Clientes:
   id_cliente primeiro_nome segundo_nome ultimo_nome     cidade  idade data_cadastro
0           1       João            Silva          Souza   São Paulo     25      2015-05-12
...
Tabela de Produtos:
   id_produto nome_produto     categoria  preco_unitario
0           1    Produto A    Eletrônicos          1500.0
...
Observações
O código gera dados sintéticos e pode ser utilizado para testar modelos de machine learning ou para simulações de dados.
A aleatoriedade do processo pode gerar resultados diferentes a cada execução, embora o seed do Faker e do random garanta a mesma sequência de geração em diferentes execuções.

