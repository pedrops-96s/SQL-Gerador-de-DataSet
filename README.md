Gerador de Dataset de Vendas
Este projeto é uma adaptação do código apresentado por Luciano Vasconcelos no workshop de DataBricks. O script tem como objetivo gerar dados fictícios para simulação de vendas em uma loja fictícia, utilizando Python e bibliotecas como Faker e Pandas.

Descrição
O projeto gera três tabelas principais:

Tabela de Vendas: Simula compras realizadas ao longo de 10 anos, com sazonalidade para eventos como Black Friday e Carnaval.
Tabela de Clientes: Gera 500 clientes fictícios, incluindo informações como nome, idade, cidade e data de cadastro.
Tabela de Produtos: Cria 50 produtos fictícios com preços variados, categorizados em diferentes segmentos, como Eletrônicos, Móveis, Roupas, Beleza, e Alimentos.
Além disso, o código realiza algumas análises como:

Total de vendas e receita por mês.
Produtos não vendidos durante o período de simulação.
Funcionalidades
Geração de dados fictícios para vendas, clientes e produtos.
Análise de vendas mensais, incluindo totais de vendas e receita.
Identificação de produtos não vendidos ao longo de 10 anos de simulação.
Tecnologias Utilizadas
Python 3.x
Pandas: Para manipulação e análise de dados.
Faker: Para geração de dados fictícios realistas.
Random: Para a criação de simulações baseadas em probabilidades.
Como Usar
Instalar as dependências:

Primeiro, clone este repositório para o seu ambiente local e instale as dependências necessárias:

bash
Copiar
git clone https://github.com/seuusuario/gerador-dataset-vendas.git
cd gerador-dataset-vendas
pip install -r requirements.txt
Executar o script:

Após as dependências estarem instaladas, você pode rodar o script para gerar as tabelas de vendas, clientes e produtos:

bash
Copiar
python gerador_dataset.py
Isso irá gerar três arquivos CSV:

tabela_vendas.csv
tabela_clientes.csv
tabela_produtos.csv
Como Funciona
O código cria uma simulação de vendas ao longo de 10 anos, com distribuição sazonal de vendas em determinados meses do ano, como Black Friday e Carnaval. As tabelas de clientes e produtos são geradas com dados aleatórios, mas realistas, usando a biblioteca Faker.

As vendas são geradas aleatoriamente com base em probabilidades de venda, e as análises são feitas com o Pandas para calcular a receita total por mês e identificar produtos não vendidos.

Análises Realizadas
Vendas por Mês: A cada mês, é calculado o total de vendas e a receita gerada.
Produtos Não Vendidos: Identificação dos produtos que não geraram vendas durante o período de 10 anos.
Exemplo de Saída
Ao final da execução, as tabelas e análises são salvas nos arquivos CSV, e as primeiras linhas de cada uma são exibidas:

Tabela de Vendas:

csv
Copiar
id_venda, id_cliente, id_produto, quantidade, data_venda
1, 53, 12, 2, 2013-01-15
2, 12, 7, 1, 2013-01-18
Tabela de Clientes:

csv
Copiar
id_cliente, primeiro_nome, segundo_nome, ultimo_nome, cidade, idade, data_cadastro
1, João, da Silva, Souza, São Paulo, 30, 2015-07-10
2, Maria, Pereira, Santos, Rio de Janeiro, 25, 2017-03-22
Tabela de Produtos:

csv
Copiar
id_produto, nome_produto, categoria, preco_unitario
1, Laptop, Eletrônicos, 1500.00
2, Sofa, Móveis, 800.50
Contribuições
Sinta-se à vontade para contribuir com melhorias, sugestões ou correções! Basta abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para mais detalhes.

Instruções adicionais:
requirements.txt: Adicione as dependências necessárias (como pandas e faker) no arquivo requirements.txt, por exemplo:

makefile
Copiar
pandas==1.5.3
faker==18.1.0
