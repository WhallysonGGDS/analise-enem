import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Caminho do arquivo CSV
caminho_csv = "C:/Users/whall/Desktop/analise_enem/dados/vendas_enem.csv"

# Ler o CSV
df = pd.read_csv(caminho_csv)

# --- Análises ---
total_vendas = df['valor'].sum()
ticket_medio = df['valor'].mean()
top_produtos = df.groupby('produto')['valor'].sum().sort_values(ascending=False).head(5)
vendas_por_vendedor = df.groupby('vendedor')['valor'].sum()

# --- Gráficos ---
# Cria a pasta 'relatorios' dentro da pasta do projeto
os.makedirs('relatorios', exist_ok=True)

plt.figure(figsize=(8,5))
top_produtos.plot(kind='bar', color='cornflowerblue')
plt.title('Top Produtos ENEM por Faturamento')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas (R$)')
plt.tight_layout()
plt.savefig('relatorios/top_produtos.png')
plt.close()

vendas_por_vendedor.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Participação de Vendas por Vendedor')
plt.ylabel('')
plt.tight_layout()
plt.savefig('relatorios/vendas_vendedor.png')
plt.close()

# --- Relatório ---
relatorio = f"""
RELATÓRIO DE VENDAS ENEM 🧾
----------------------------
Total de Vendas: R$ {total_vendas:,.2f}
Ticket Médio: R$ {ticket_medio:,.2f}

Top Produtos:
{top_produtos}

Vendas por Vendedor:
{vendas_por_vendedor}

Gráficos gerados: top_produtos.png | vendas_vendedor.png
"""

# Salva o relatório dentro da pasta do projeto
with open('relatorios/relatorio_enem.txt', 'w', encoding='utf-8') as f:
    f.write(relatorio)

print("✅ Relatório ENEM gerado com sucesso! Confira a pasta 'analise_enem/relatorios'.")
