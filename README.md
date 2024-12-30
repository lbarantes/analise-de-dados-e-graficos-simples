# Análise de Vendas - Python Script

Este projeto é um script em Python utilizado para analisar dados de vendas contidos em um arquivo Excel. Utilizando as bibliotecas **Pandas** para manipulação de dados e **Matplotlib** para visualização, o script realiza cálculos sobre faturamento e vendas, além de gerar gráficos para facilitar a análise.

## ⚒️ Funcionalidades

1. **Cálculos de Faturamento**  
   - **Faturamento Total**: O script calcula o total de vendas de todos os produtos.
   - **Faturamento por Loja**: Calcula o faturamento por loja e ordena os resultados.
   - **Faturamento por Produto**: Calcula o faturamento de cada produto por loja.

2. **Cálculos de Vendas**  
   - **Vendas por Loja**: Realiza o cálculo da quantidade total de produtos vendidos por loja.
   - **Vendas por Produto**: Realiza o cálculo da quantidade total de cada produto vendido.

3. **Geração de Gráficos**  
   - **Gráfico de Vendas por Produto**: Gera um gráfico de barras mostrando a quantidade de vendas por produto.
   - **Gráfico de Vendas por Loja**: Gera um gráfico de barras mostrando a quantidade de vendas por loja.
   - **Gráfico de Faturamento por Produto**: Gera um gráfico de barras mostrando o faturamento por produto.
   - **Gráfico de Faturamento por Loja**: Gera um gráfico de barras mostrando o faturamento por loja.

Os gráficos são salvos em arquivos PNG no mesmo diretório do script.

## 📊 Visualizações Geradas
- **Gráfico de Vendas por Produto**: `vendas_por_produto.png`
- **Gráfico de Vendas por Loja**: `vendas_por_loja.png`
- **Gráfico de Faturamento por Produto**: `faturamento_por_produto.png`
- **Gráfico de Faturamento por Loja**: `faturamento_por_loja.png`

## 💻 Tecnologias Utilizadas

- **Pandas**: Para manipulação de dados, cálculos e agregações.
- **Matplotlib**: Para geração de gráficos de vendas e faturamento.

## 📂 Arquivo de Entrada

O script espera que o arquivo Excel `vendas.xlsx` contenha as seguintes colunas:
- **Loja**: Identificação da loja onde as vendas ocorreram.
- **Produto**: Nome do produto vendido.
- **Quantidade**: Quantidade de unidades vendidas.
- **Valor Final**: Valor total da venda para o produto.

## 📝 Exemplo de Saída no Console

```plaintext
Faturamento total:
123456.78

Faturamento por loja:
           Valor Final
Loja                  
Loja A       12345.67
Loja B       23456.78

Faturamento por produto:
                   Valor Final
Produto Loja               
Produto 1 Loja A  1234.56
Produto 1 Loja B  2345.67

Vendas por loja:
           Quantidade
Loja                  
Loja A           123
Loja B           456

Vendas por produto:
         Quantidade
Produto            
Produto 1        123
Produto 2        456
