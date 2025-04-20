"""
Gera visualização interativa da média mensal do preço do Diesel por estado (UF),
a partir do arquivo diesel_anp_consolidado.csv.
"""

import pandas as pd
import plotly.express as px

# Caminho do CSV consolidado
CAMINHO_ARQUIVO = r"C:\Users\Emanuel\Documents\InteligenciaMercado\data\transport\anp_diesel_raw\diesel_anp_consolidado.csv"

# Carrega os dados
df = pd.read_csv(CAMINHO_ARQUIVO, sep=";", encoding="utf-8-sig")

# Converte datas
df["DATA INICIAL"] = pd.to_datetime(df["DATA INICIAL"], dayfirst=True, errors="coerce")

# Cria coluna Ano-Mês
df["ANO_MES"] = df["DATA INICIAL"].dt.to_period("M").dt.to_timestamp()

# Garante que o preço é numérico
df["PREÇO MÉDIO REVENDA"] = pd.to_numeric(df["PREÇO MÉDIO REVENDA"], errors="coerce")

# Agrupa média por mês e estado
df_agrupado = df.groupby(["ANO_MES", "ESTADO"])["PREÇO MÉDIO REVENDA"].mean().reset_index()

# Cria gráfico interativo
fig = px.line(
    df_agrupado,
    x="ANO_MES",
    y="PREÇO MÉDIO REVENDA",
    color="ESTADO",
    title="Média Mensal do Preço do Diesel por Estado (UF)",
    labels={"ANO_MES": "Data", "PREÇO MÉDIO REVENDA": "Preço Médio (R$)", "ESTADO": "UF"},
    hover_name="ESTADO"
)

# Exibe
fig.update_layout(xaxis_title="Mês", yaxis_title="Preço Médio (R$)", hovermode="x unified")
fig.show()
