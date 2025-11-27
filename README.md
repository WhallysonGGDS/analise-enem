# 📊 Análise de Vendas ENEM — Python & Pandas

Projeto desenvolvido para analisar um conjunto de dados de vendas relacionadas ao ENEM, gerando métricas essenciais, rankings, gráficos automáticos e um relatório completo.  
Ideal para portfólio de **Analista de Dados Júnior**, mostrando domínio em **Pandas, Matplotlib, manipulação de dados e geração de insights**.

## 🚀 Funcionalidades Principais

- ✔️ Leitura automática do dataset de vendas  
- ✔️ Cálculo de métricas essenciais:
  - **Total de vendas**
  - **Ticket médio**
  - **Top 5 produtos mais lucrativos**
  - **Vendas por vendedor**
- ✔️ Geração automática de gráficos:
  - 📈 Top produtos mais vendidos  
  - 🥧 Participação percentual por vendedor
- ✔️ Criação de relatório completo em `.txt`
- ✔️ Pasta `relatorios/` criada automaticamente

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **OS**

## 📂 Estrutura do Projeto

```
/
├── analise_enem.py
├── dados/
│   └── vendas_enem.csv
└── relatorios/
    ├── top_produtos.png
    ├── vendas_vendedor.png
    └── relatorio_enem.txt
```

## 🛠️ Como Executar o Projeto

1. Tenha o Python instalado (3.10+ recomendado)  
2. Instale as dependências:

```bash
pip install pandas numpy matplotlib
```

3. Ajuste o caminho do CSV se necessário:

```python
caminho_csv = "C:/Users/whall/Desktop/Analise_de_Vendas/dados/vendas_enem.csv"
```

4. Rode o script:

```bash
python analise_enem.py
```

5. Veja os relatórios gerados na pasta:

```
./relatorios/
```

## 📊 Exemplos de Saída

- **top_produtos.png**  
- **vendas_vendedor.png**  
- **relatorio_enem.txt**

## 🧾 Sobre o Dataset

O arquivo **vendas_enem.csv** deve conter as seguintes colunas:

| coluna   | descrição |
|----------|-----------|
| produto  | Nome do produto vendido |
| valor    | Valor unitário da venda |
| vendedor | Quem realizou a venda |

## 🤝 Contribuições

Sugestões e melhorias são sempre bem-vindas!

## 🧑‍💻 Autor

**Whallyson Gabriel Garcia da Silva**  
Analista de Dados • Brasil  
GitHub: https://github.com/WhallysonGGDS
