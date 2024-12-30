import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_excel('E:/Python/Projetos/Clayton/Curso Analise de Dados/Aula 1/vendas.xlsx')

# Calculando faturamento total
faturamentoTotal = data['Valor Final'].sum()

print("Faturamento total:")
print(faturamentoTotal)

# Calculando faturamento p/loja
faturamentoPorLoja = data[['Loja', 'Valor Final']].groupby('Loja').sum().sort_values(by='Valor Final', ascending=True)

print("Faturamento por loja:")
print(faturamentoPorLoja)

# Calculando faturamento p/produto
faturamentoPorProduto = data[['Loja', 'Produto', 'Valor Final']].groupby(['Produto', 'Loja']).sum()

print("Faturamento por produto:")
print(faturamentoPorProduto)

# Calculando vendas p/loja
vendasPorLoja = data[['Loja', 'Quantidade']].groupby('Loja').sum().sort_values(by='Quantidade', ascending=True)

print("Vendas por loja:")
print(vendasPorLoja)

# Calculando vendas p/produto
vendasPorProduto = data[['Produto', 'Quantidade']].groupby(['Produto']).sum()

print("Vendas por produto:")
print(vendasPorProduto)
    
print("Gerando Gráfico de vendas p/produto...")
plot.figure(figsize=(10, 6))
plot.bar(data['Produto'], data['Quantidade'])
plot.xlabel('Produto')
plot.ylabel('Quantidade')
plot.title('Gráfico de vendas p/produto')
plot.savefig("vendas_por_produto.png")
print("Gráfico gerado!")
    
print("Gerando Gráfico de vendas p/loja...")
plot.figure(figsize=(13, 6))
plot.bar(data['Loja'], data['Quantidade'])
plot.xlabel('Loja')
plot.ylabel('Quantidade')
plot.title('Gráfico de vendas p/loja')
plot.savefig("vendas_por_loja.png")
print("Gráfico gerado!")
    
print("Gerando Gráfico de faturamento p/produto...")
plot.figure(figsize=(13, 6))
plot.bar(data['Produto'], data['Valor Final'])
plot.xlabel('Produto')
plot.ylabel('Quantidade')
plot.title('Gráfico de faturamento p/produto')
plot.savefig("faturamento_por_produto.png")
print("Gráfico gerado!")
    
print("Gerando Gráfico de faturamento p/loja...")
plot.figure(figsize=(13, 6))
plot.bar(data['Loja'], data['Valor Final'])
plot.xlabel('Loja')
plot.ylabel('Quantidade')
plot.title('Gráfico de faturamento p/loja')
plot.savefig("faturamento_por_loja.png")
print("Gráfico gerado!")