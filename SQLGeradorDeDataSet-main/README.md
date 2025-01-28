# Gerador de Dataset de Vendas

Este projeto gera dados simulados para vendas de uma loja fictícia, utilizando o pacote `Faker` para a geração de dados aleatórios e o `pandas` para manipulação de tabelas. O código cria três tabelas principais: **Vendas**, **Clientes** e **Produtos**. Além disso, realiza uma análise simples sobre as vendas, como a receita total por mês e os produtos que não foram vendidos.

## Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: Para manipulação de dados e criação de tabelas.
- **Faker**: Para gerar dados fictícios de clientes e produtos.
- **Random**: Para gerar valores aleatórios.

## Estrutura do Projeto

1. **gerador_dataset.py**: Script principal para gerar as tabelas de vendas, clientes e produtos, além de realizar algumas análises sobre os dados.
   
2. **Arquivos CSV gerados**:
    - **tabela_vendas.csv**: Contém as informações sobre as vendas realizadas.
    - **tabela_clientes.csv**: Contém os dados dos clientes que realizaram compras.
    - **tabela_produtos.csv**: Contém a lista de produtos disponíveis na loja.

## Descrição das Funções

### 1. `gerar_tabela_vendas()`
   - **Objetivo**: Gerar a tabela de vendas com base em uma distribuição sazonal, com maior volume de vendas durante datas como Black Friday e Carnaval.
   - **Gera**: 
     - ID da venda
     - ID do cliente (500 clientes únicos)
     - ID do produto (com exceção dos produtos excluídos)
     - Quantidade comprada
     - Data da venda (dentro do intervalo de 2013 a 2023)

### 2. `gerar_tabela_clientes()`
   - **Objetivo**: Gerar a tabela de clientes com dados fictícios, incluindo nome, cidade, idade e data de cadastro.
   - **Gera**:
     - ID do cliente
     - Nome completo (primeiro nome, segundo nome e sobrenome)
     - Idade (entre 18 e 65 anos)
     - Cidade
     - Data de cadastro (entre 2012 e 2023)

### 3. `gerar_tabela_produtos()`
   - **Objetivo**: Gerar a tabela de produtos com categorias e preços aleatórios.
   - **Gera**:
     - ID do produto
     - Nome do produto
     - Categoria do produto (Eletrônicos, Móveis, Roupas, Beleza ou Alimentos)
     - Preço unitário

### 4. **Análise de Vendas**
   - O código realiza uma análise das vendas por mês, calculando a **quantidade total vendida** e a **receita total**.
   - Também exibe quais produtos não foram vendidos durante o período.

## Como Usar

1. Clone o repositório ou baixe o arquivo `gerador_dataset.py` para o seu computador.
2. Certifique-se de que você tem o Python 3.x e as bibliotecas `pandas` e `faker` instaladas. Caso não tenha, instale com:
   
   ```bash
   pip install pandas faker


### Execute o script gerador_dataset.py com o seguinte comando:
```bash
   python gerador_dataset.py




