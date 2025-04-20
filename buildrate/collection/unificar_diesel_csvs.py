"""
Unifica todos os CSVs de Diesel da ANP, converte datas corretamente
(mesmo com formatos mistos), aplica filtro a partir de 01/01/2010,
e exporta resultado com separador ';'.
"""

import pandas as pd
import os
from glob import glob

# Caminho base
BASE_PATH = r"C:\Users\Emanuel\Documents\InteligenciaMercado\data\transport\anp_diesel_raw"
csv_files = sorted(glob(os.path.join(BASE_PATH, "20*-20*.csv")))

df_list = []

def converter_data(col):
    """
    Converte a coluna de data corretamente, seja número serial do Excel
    (ex: 38116), ou string legível (ex: 31/12/2023).
    """
    col = col.astype(str).str.strip()

    # Tenta como número do Excel
    try:
        numeros = pd.to_numeric(col, errors="coerce")
        # Se a maioria dos valores estiverem na faixa de datas Excel:
        if numeros.dropna().between(30000, 50000).mean() > 0.5:
            return pd.to_datetime(numeros, origin="1899-12-30", unit="d", errors="coerce")
    except Exception:
        pass

    # Caso contrário, tenta como string legível (dd/mm/yyyy)
    return pd.to_datetime(col, dayfirst=True, errors="coerce")


print("🔁 Unificando arquivos:")
for csv_file in csv_files:
    print(f" - {os.path.basename(csv_file)}")
    df = pd.read_csv(csv_file, sep=";", dtype=str)

    # Normaliza colunas
    df.columns = df.columns.str.strip().str.upper()

    # Converte "DATA INICIAL"
    if "DATA INICIAL" not in df.columns:
        raise KeyError(f"❌ Coluna 'DATA INICIAL' não encontrada no arquivo {csv_file}")

    df["DATA INICIAL"] = converter_data(df["DATA INICIAL"])

    df_list.append(df)

# Unir todos os arquivos
df_final = pd.concat(df_list, ignore_index=True)

# Aplicar filtro de data
df_final = df_final[df_final["DATA INICIAL"] >= pd.Timestamp("2010-01-01")]

# Exportar consolidado
output_path = os.path.join(BASE_PATH, "diesel_anp_consolidado.csv")
df_final.to_csv(output_path, sep=";", encoding="utf-8-sig", index=False)

print(f"\n✅ Arquivo final salvo: {output_path}")
