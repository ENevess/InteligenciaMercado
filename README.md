# 🧠 Inteligência de Mercado — Transporte e Energia

Este projeto tem como objetivo centralizar, processar e analisar dados econômicos e logísticos críticos para o setor de **transporte rodoviário de cargas no Brasil**, com foco em **Diesel**, **Petróleo Brent**, **Frete Rodoviário** e **Indicadores Econômicos**.

## 📦 Estrutura

```
InteligenciaMercado/
├── buildrate/               # Scripts de coleta e utilitários
├── data/                    # Dados armazenados (.csv)
│   ├── transport/           # Diesel, petróleo, frete
│   ├── macro/               # IPCA, PIB, etc.
│   └── ...
├── notebooks/               # Explorações e análises
├── models/                  # (em breve)
├── reports/                 # Relatórios e dashboards
├── README.md                # Este documento
└── requirements.txt         # Dependências do projeto
```

## 📈 Fontes de Dados

| Tema            | Fonte                                            | Formato     |
|----------------|--------------------------------------------------|-------------|
| Diesel (preço)  | ANP (Agência Nacional do Petróleo)              | XLSB/XLSX   |
| Petróleo Brent  | Investing.com / EIA                             | CSV         |
| Frete Rodoviário| ONTL (Observatório Nacional de Transporte)      | JSON via API|
| IPCA, PIB, etc  | Banco Central do Brasil (SGS)                   | API         |

## 🔍 Definições importantes

### TKU — Tonelada Quilômetro Útil
Unidade-padrão usada no transporte de cargas. Define o volume transportado multiplicado pela distância percorrida:

```
TKU = toneladas transportadas × quilômetros percorridos
```

Exemplo: transportar 10 toneladas por 300 km = 3.000 TKU

Se o frete médio é R$ 0,25 por TKU → custo total = R$ 750,00

---

## 🚀 Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/InteligenciaMercado.git
cd InteligenciaMercado
```

2. Crie o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Execute os coletores:
```bash
python buildrate/collection/collect_diesel_anp.py
python buildrate/collection/collect_brent.py
python buildrate/collection/collect_frete_ontl.py
```

---

## 📌 Observações

- Todos os dados utilizados são públicos e de fontes oficiais.
- Os arquivos `.csv` e `.xls[x|b]` estão incluídos por decisão estratégica, pois são parte integrante do pipeline de transformação e análise.

---

## 📬 Contato

Para sugestões, dúvidas ou contribuições:
- [ENevess](https://github.com/ENevess)
