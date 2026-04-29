import pandas as pd

dados = {
    'Produto': ['Caderno', 'Caneta', 'Lápis'],
    'Quantidade': [10, 50, 30],
    'Preço': [15.50, 2.00, 1.50]
}

df = pd.DataFrame(dados)

print("--- Relatório de Vendas V5 ---")
print(df)
print("\nMédia de produtos no estoque:", df['Quantidade'].mean())

def calcular_desconto(valor, percentual):
    if percentual < 0:
        return valor
    return valor - (valor * (percentual / 100))

def validar_email(email):
    return "@" in email and "." in email

def formatar_moeda(valor):
    return f"R$ {valor:.2f}"