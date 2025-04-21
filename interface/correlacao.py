
# interface/correlacao.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mapa de Correlações", layout="wide")
st.title("📊 Mapa de Correlações entre Indicadores Econômicos")

# Arquivos e colunas personalizadas
arquivos = {
    "EURO": ("data/exchange_rates/eur_brl.csv", None),
    "DOLAR": ("data/exchange_rates/usd_brl.csv", None),
    "SELIC": ("data/interest_rates/selic.csv", None),
    "DIESEL": ("data/transport/diesel_anp_consolidado.csv", {"data": "DATA FINAL", "valor": "PREÇO MÉDIO REVENDA"}),
    "PIB": ("data/macro/pib.csv", None),
    "IBC_BR": ("data/macro/ibcbr.csv", None),
    "DESEMPREGO": ("data/macro/unemployment_rate_pnadc_ipea.csv", {"data": "data", "valor": "taxa_desemprego"}),
    "CREDITO_EMP": ("data/credit/credito_empresas.csv", None),
    "IPCA": ("data/macro/ipca.csv", None),
    "IGPM": ("data/macro/igpm.csv", None),
    "PROD_IND": ("data/macro/producao_industrial.csv", None)
}

@st.cache_data
def carregar_dados():
    df_final = pd.DataFrame()

    for nome, (caminho, colunas) in arquivos.items():
        try:
            df = pd.read_csv(caminho, sep=";" if "diesel" in caminho else ",")
            if colunas:
                col_data = colunas["data"]
                col_valor = colunas["valor"]
            else:
                col_data = [col for col in df.columns if col.lower() in ["data", "date"]][0]
                col_valor = [col for col in df.columns if col.lower() in ["valor", "value"]][0]

            df = df.rename(columns={col_data: "DATE", col_valor: nome})
            df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
            df = df[["DATE", nome]].dropna()

            if df_final.empty:
                df_final = df
            else:
                df_final = pd.merge(df_final, df, on="DATE", how="outer")

        except Exception as e:
            st.warning(f"Erro ao carregar {nome}: {e}")

    df_final = df_final.dropna().sort_values("DATE")
    df_final = df_final.set_index("DATE")
    return df_final

# Carregar os dados
df = carregar_dados()

# Verificar se o DataFrame está válido
if df.empty:
    st.error("❌ Nenhum dado válido encontrado para análise de correlação.")
    st.stop()

# Filtro de período
min_date, max_date = df.index.min(), df.index.max()
range_values = st.slider(
    "Selecione o período de análise:",
    min_value=min_date.to_pydatetime(),
    max_value=max_date.to_pydatetime(),
    value=(min_date.to_pydatetime(), max_date.to_pydatetime()),
    format="YYYY-MM"
)

df_periodo = df.loc[range_values[0]:range_values[1]]

# Matriz de correlação
st.subheader("🔍 Correlação entre indicadores (Pearson)")
cor = df_periodo.corr()

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(cor, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, ax=ax)
st.pyplot(fig)
