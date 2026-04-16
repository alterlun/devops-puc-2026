import pandas as pd

dados = {
    'Produto': ['Caderno', 'Caneta', 'Lápis'],
    'Quantidade': [10, 50, 30],
    'Preço': [15.50, 2.00, 1.50]
}

df = pd.DataFrame(dados)

print("--- Relatório de Vendas ---")
print(df)
print("\nMédia de produtos no estoque:", df['Quantidade'].mean())