"""
Coleta histórica do preço do petróleo Brent via API da EIA (EIA.gov)
e salva os dados no formato padronizado do projeto.

Fonte: https://www.eia.gov/opendata/
Série: PET.RBRENT.D (Brent Spot Price - USD)
Periodicidade: Diária
Filtro: a partir de 01/01/2010
"""

import requests
import pandas as pd
import os

# Configurações da API
API_KEY = "kTvWceAgEa207fjvURRNdEmEnXcsSQFAdYIPaf5x"
SERIE_ID = "PET.RBRENT.D"
URL = f"https://api.eia.gov/series/?api_key={API_KEY}&series_id={SERIE_ID}"

def coletar_dados_brent():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Erro ao acessar a API da EIA: {response.status_code}")

    try:
        dados = response.json()["series"][0]["data"]
    except (KeyError, IndexError):
        raise Exception("❌ Erro ao extrair os dados da resposta da API.")

    # Monta DataFrame
    df = pd.DataFrame(dados, columns=["DATA", "PRECO_FECHAMENTO_USD"])
    df["DATA"] = pd.to_datetime(df["DATA"], format="%Y%m%d")
    df["PRECO_FECHAMENTO_USD"] = pd.to_numeric(df["PRECO_FECHAMENTO_USD"], errors="coerce")

    # Filtra dados a partir de 01/01/2010
    df = df[df["DATA"] >= pd.Timestamp("2010-01-01")]

    # Ordena
    df = df.sort_values("DATA").reset_index(drop=True)

    return df

if __name__ == "__main__":
    df_brent = coletar_dados_brent()

    # Caminho de saída no projeto
    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../data/transport/preco_petroleo_brent.csv")
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df_brent.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")

    print(f"\n✅ Dados do Brent salvos com sucesso em: {output_path}")
    print(df_brent.tail())
