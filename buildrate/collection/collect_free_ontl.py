"""
Coleta dados de preço médio do frete rodoviário (R$/TKU) via API da ONTL.
Modal: Rodoviário
Periodicidade: Mensal
Cobertura: A partir de 2010
"""

import requests
import pandas as pd
import os
import json

# URL da API da ONTL para frete médio
URL = "https://ontl-apim.infrasa.gov.br/api/apims/children/1052/997%20-%20Frete%20M%C3%A9dio%20-%20R$%20-%20TKU/json"

def coletar_dados_ontl():
    response = requests.get(URL)
    response.raise_for_status()

    # Decodifica e carrega JSON
    raw_data = json.loads(response.content.decode("utf-8"))
    df = pd.DataFrame(raw_data)

    # Renomeia e seleciona colunas
    df = df.rename(columns={
        "Ano": "ANO",
        "Mês": "MES",
        "Grupo Mercadoria": "GRUPO_MERCADORIA",
        "Frete Médio Rodovias R$/TKU": "FRETE_MEDIO_RODOVIAS_TKU"
    })

    df = df[["ANO", "MES", "GRUPO_MERCADORIA", "FRETE_MEDIO_RODOVIAS_TKU"]]

    # Converter valores e filtrar apenas positivos
    df["FRETE_MEDIO_RODOVIAS_TKU"] = pd.to_numeric(df["FRETE_MEDIO_RODOVIAS_TKU"], errors="coerce")
    df = df[df["FRETE_MEDIO_RODOVIAS_TKU"] > 0]

    # Criar coluna de data
    df["DATA"] = pd.to_datetime(dict(year=df["ANO"], month=df["MES"], day=1))

    # Ordenar cronologicamente
    df = df.sort_values("DATA").reset_index(drop=True)

    return df

if __name__ == "__main__":
    df_frete = coletar_dados_ontl()

    # Arredonda frete para 3 casas decimais
    df_frete["FRETE_MEDIO_RODOVIAS_TKU"] = df_frete["FRETE_MEDIO_RODOVIAS_TKU"].round(3)

    # Caminho de saída
    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../data/transport/frete_medio_ontl.csv")
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df_frete.to_csv(output_path, sep=";", index=False, encoding="utf-8-sig")

    print(f"\n✅ Arquivo salvo com sucesso: {output_path}")
    print(df_frete.tail())
