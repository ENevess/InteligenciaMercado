
# models/simulation/treinar_modelo_regressao.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Caminhos atualizados
EURO_PATH = "data/exchange_rates/eur_brl.csv"
DOLAR_PATH = "data/exchange_rates/usd_brl.csv"
SELIC_PATH = "data/interest_rates/selic.csv"
DIESEL_PATH = "data/transport/diesel_anp_consolidado.csv"
OUTPUT_DIR = "models/simulation/"

# Carregar e padronizar euro, dólar, selic
euro = pd.read_csv(EURO_PATH).rename(columns={"data": "DATE", "valor": "EURO"})
dolar = pd.read_csv(DOLAR_PATH).rename(columns={"data": "DATE", "valor": "DOLAR"})
selic = pd.read_csv(SELIC_PATH).rename(columns={"data": "DATE", "valor": "SELIC"})

euro["DATE"] = pd.to_datetime(euro["DATE"])
dolar["DATE"] = pd.to_datetime(dolar["DATE"])
selic["DATE"] = pd.to_datetime(selic["DATE"])

# Carregar diesel com separador correto e renomear colunas
diesel = pd.read_csv(DIESEL_PATH, sep=";")
diesel = diesel.rename(columns={
    "DATA FINAL": "DATE",
    "PREÇO MÉDIO REVENDA": "DIESEL"
})
diesel["DATE"] = pd.to_datetime(diesel["DATE"], errors="coerce", dayfirst=True)
diesel = diesel[(diesel["DATE"] >= "2010-01-01") & (diesel["DATE"] <= "2030-01-01")]

# Agrupar diesel por mês
diesel_mensal = (
    diesel.groupby(pd.Grouper(key="DATE", freq="ME"))["DIESEL"]
    .mean()
    .reset_index()
)

# Merge dos dados
df = euro.merge(dolar, on="DATE").merge(selic, on="DATE").merge(diesel_mensal, on="DATE")
df = df[["DATE", "DIESEL", "SELIC", "DOLAR", "EURO"]].dropna().sort_values("DATE")

# Salvar matriz de correlação
correlacoes = df[["DIESEL", "SELIC", "DOLAR", "EURO"]].corr()
correlacoes.to_csv("models/simulation/correlacoes.csv")

# Treinamento dos modelos
targets = ["EURO", "DOLAR", "SELIC", "DIESEL"]
for target in targets:
    features = [col for col in targets if col != target]
    X = df[features]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    joblib.dump(model, f"{OUTPUT_DIR}modelo_regressao_{target.lower()}.joblib")
    print(f"✅ Modelo salvo: {target}")
