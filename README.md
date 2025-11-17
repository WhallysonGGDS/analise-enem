# 📊 Análise de Vendas ENEM — Python + Pandas + Matplotlib

Projeto completo de **Análise Exploratória de Dados (EDA)** usando Python, focado em entender o desempenho de vendas de produtos educacionais do ENEM.

Aqui você encontra tudo o que um analista de dados de verdade faz no dia a dia: limpeza, organização, KPIs, gráficos, insights e automação do fluxo.

---

## 🚀 Objetivo do Projeto

O foco é gerar valor de negócio através da análise dos dados:

- 📦 Entender os produtos que mais vendem  
- 💰 Calcular faturamento total e ticket médio  
- 🏆 Descobrir os top produtos  
- 🧑‍💼 Avaliar desempenho por vendedor  
- 📅 Analisar a distribuição temporal das vendas  
- 📈 Criar visualizações para facilitar a tomada de decisão  

---

## 🧠 Tecnologias Utilizadas

- **Python 3.x**  
- **Pandas** — limpeza + manipulação dos dados  
- **NumPy** — funções matemáticas  
- **Matplotlib** — gráficos  
- **OS** — automação de diretórios  

---

## 📂 Estrutura do Projeto

analise_enem/
│
├── dados/
│ └── vendas_enem.csv # Arquivo base original
│
├── relatorios/ # Gráficos gerados automaticamente
│ ├── top_produtos.png
│ ├── vendas_por_vendedor.png
│ └── distribuicao_temporal.png
│
├── analise_enem.py # Script principal da análise
└── README.md # Este arquivo lindo que você está lendo


---

## 🔍 Etapas da Análise

### 1️⃣ Carregamento e limpeza dos dados  
- Conferência de colunas  
- Conversão de tipos  
- Padronização das datas  

### 2️⃣ Cálculo dos KPIs principais  
```python
total_vendas = df['valor'].sum()
ticket_medio = df['valor'].mean()

3️⃣ Top produtos

Agrupamento por produto para achar os mais rentáveis.

4️⃣ Desempenho por vendedor

Gráfico em pizza ou barras comparando faturamento individual.

5️⃣ Visualizações

Todos os gráficos são exportados para a pasta relatorios/ automaticamente.

📊 Exemplos de Gráficos

Top Produtos

Vendas por Vendedor

Distribuição Temporal das Vendas

Os arquivos são salvos automaticamente a cada execução.

⚙️ Como Executar o Projeto

1.Clone o repositório:

git clone https://github.com/WhallysonGGDS/analise-enem.git

2. Instale as dependências:

pip install pandas numpy matplotlib

3. Execute o script:

python analise_enem.py

4. Veja os gráficos gerados na pasta relatorios/.

💡 Insights Gerados

Produtos mais caros nem sempre são os que mais vendem.

Determinados vendedores têm clara dominância de faturamento.

As vendas possuem sazonalidade semanal.

O ticket médio revela oportunidades de upsell.

Sempre focado na tomada de decisão, não só em números.

🧑‍💻 Autor

Gabriel Garcia (Whallyson)
Analista de Dados • Python Lover • Builder de Projetos Reais
📍 Goiânia — GO

⭐ Quer contribuir?

Fique à vontade para abrir issues, enviar sugestões ou mandar aquele PR maroto.

Se curtir o projeto, deixa uma ⭐ no repo — ajuda demais! 🚀✨