
# Projeto Inteligência de Mercado

Este repositório contém a estrutura de um sistema automatizado para coleta, organização e análise de dados econômicos que impactam o setor de produção de caminhões. O projeto visa antecipar cenários de mercado com base em dados públicos e internos, fornecendo suporte técnico à alta gestão.

## 🎯 Objetivo

Correlacionar dados macroeconômicos com variáveis internas de produção (build rate e mix), possibilitando análises preditivas, simulações e relatórios de apoio à tomada de decisão estratégica.

## 🏗️ Estrutura do Projeto

```
.
├── buildrate/                 # Scripts de coleta de dados por tema
│   ├── collect_agropecuaria.py
│   ├── collect_credito_empresas.py
│   └── ...
├── utils/                     # Funções auxiliares (ex: sgs_downloader)
├── data/                      # Armazenamento local em CSV (por tema)
├── notebooks/                 # Análises exploratórias e validações
├── models/                    # Modelos preditivos futuros
├── reports/                   # Relatórios executivos
├── logs/                      # Histórico de execuções (futuro)
├── runner.py                 # Orquestrador central de coleta
└── docs/                      # Documentação e apresentações
```

## ⚙️ Execução

### Ambiente virtual

Antes de iniciar, instale as dependências:
```bash
pip install -r requirements.txt
```

### Coleta de dados

Para coletar os dados individualmente:
```bash
python -m buildrate.collection.collect_credito_empresas
```

Para executar todos os scripts automaticamente:
```bash
python runner.py
```

## 📊 Indicadores Utilizados

- Câmbio: USD/BRL, EUR/BRL
- Inflação e Juros: IPCA, Selic, CDI, IGP-M
- Atividade Econômica: PIB, IBC-Br, Consumo, Produção Industrial
- Crédito PJ (SGS 20616)
- Emprego (PNAD Contínua via IPEA)
- Frete Médio Rodoviário (ONTL)
- Petróleo Brent (EIA)
- Diesel (ANP)

## 🚧 Problemas Conhecidos

- Exportações SGS 22601 e 22663 (erros 504)
- Série SGS 24369 substituída por IPEA

## 📈 Próximos Passos

- Integração com dados internos da montadora
- Versionamento automático dos dados
- Dashboards interativos com simulação de cenários
- Camada de transformação separada dos coletores
- Migração para SQL Server ou Snowflake

## 📎 Diagrama de Arquitetura

![Diagrama](diagrama_arquitetura_projeto.png)

## 🧠 Licença

Uso interno. Desenvolvido pela equipe de TI para suporte à diretoria executiva.
