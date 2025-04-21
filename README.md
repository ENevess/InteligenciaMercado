
# 📊 Inteligência de Mercado - Análise Econômica e Simulação de Cenários

Este projeto tem como objetivo oferecer uma ferramenta robusta e interativa para análise de indicadores macroeconômicos e simulação de cenários que impactam diretamente a indústria de caminhões no Brasil.

---

## 🎯 Objetivo

O projeto busca apoiar a tomada de decisão estratégica, permitindo:

- Simulação de impactos econômicos (ex: variação da SELIC, câmbio, diesel)
- Previsão de comportamento de indicadores como EURO, DÓLAR, DIESEL e SELIC
- Visualização da correlação entre variáveis econômicas
- Exploração interativa dos dados históricos coletados

---

## 🧠 Funcionalidades do MVP

### 🔧 Simulador de Cenário

- Previsão de uma variável (EURO, DÓLAR, DIESEL, SELIC)
- Input manual de outras variáveis para análise de impacto
- Comentário automático interpretando o resultado
- Gráfico com tendência futura
- Índice de correlação com as variáveis de entrada

### 📈 Mapa de Correlações

- Visualização de heatmap entre todos os indicadores coletados
- Filtro de período de análise
- Comentário explicativo bilíngue para usuários não técnicos

---

## 🌍 Idiomas suportados

- Português 🇧🇷
- Inglês 🇺🇸

---

## 🗃️ Indicadores disponíveis

- Câmbio: EUR/BRL, USD/BRL
- Juros: SELIC
- Combustíveis: Preço Médio do Diesel (ANP)
- Inflação: IPCA, IGP-M
- Atividade Econômica: PIB, IBC-Br, Produção Industrial
- Crédito: Concessão para Empresas
- Mercado de Trabalho: Taxa de Desemprego (PNAD Contínua - IPEA)

---

## 📂 Estrutura de Diretórios

```
InteligenciaMercado/
│
├── buildrate/             # Scripts de coleta de dados
├── data/                  # Dados organizados por tema (exchange_rates, macro, transport, etc.)
├── interface/             # Aplicação Streamlit (visualização)
│   └── streamlit_app.py
├── models/                # Modelos de simulação e predição
│   └── simulation/
├── notebooks/             # Explorações auxiliares
├── reports/               # Relatórios gerados
├── runner.py              # Execução central dos scripts de coleta
└── README.md              # Documentação do projeto
```

---

## 🚀 Como Executar Localmente

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Execute a aplicação
```bash
streamlit run interface/streamlit_app.py
```

---

## 📌 Observações

- Os dados são públicos e coletados via APIs (BCB, IPEA, IBGE, ANP) ou extraídos de planilhas oficiais
- Todas as previsões são **estimativas simplificadas** baseadas em modelos de regressão linear (MVP)
- O projeto está preparado para evoluir com novos modelos e mais granularidade

---

## 🧪 Próximos Passos

- Adição de novos indicadores (ex: produção caminhões, mix por segmento)
- Substituição dos modelos lineares por RandomForest/XGBoost
- Exportação dos cenários em PDF ou XLS
- Dashboard histórico interativo por série

---

## 🤝 Contribuição

Fique à vontade para sugerir melhorias, abrir issues ou contribuir com código!

---

## 🛡️ Licença

Este projeto utiliza dados públicos e não possui restrições de uso para fins educacionais ou analíticos internos.
