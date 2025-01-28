Gerador de Dataset de Vendas Fictícias
Este projeto foi desenvolvido como parte de uma adaptação do conteúdo apresentado por Luciano Vasconcelos no workshop de DataBricks. Ele gera dados fictícios para simulação de vendas, clientes e produtos de uma loja fictícia. O código simula dados ao longo de 10 anos, com sazonalidade, para análise de vendas, incluindo Black Friday e Carnaval.

Descrição
O objetivo do projeto é criar um gerador de dados fictícios para análise de vendas de uma loja fictícia. O script utiliza Python, Faker e Pandas para gerar:

Tabela de Vendas: Registra as compras realizadas ao longo de 10 anos, incluindo dados sobre o produto, cliente, quantidade e data.
Tabela de Clientes: Gera 500 clientes fictícios com dados como nome, cidade, idade e data de cadastro.
Tabela de Produtos: Cria 50 produtos fictícios, com categorias variadas e preços entre diferentes faixas.
Além disso, o código também realiza algumas análises de vendas, como a receita total por mês e a quantidade de produtos não vendidos.

Funcionalidades
Geração de dados de vendas, clientes e produtos fictícios.
Cálculos de vendas mensais, incluindo total de vendas e receita.
Identificação de produtos não vendidos.
Geração de relatórios em CSV das tabelas geradas.
Tecnologias Utilizadas
Python 3.x
Pandas: Para manipulação e análise dos dados.
Faker: Para geração de dados realistas de clientes, produtos e datas.
Random: Para a geração de vendas e dados aleatórios.
Como Usar
Clone o repositório:

Clone este projeto para sua máquina local usando o comando:
