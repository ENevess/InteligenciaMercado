"""
Extrai os dados de Diesel dos arquivos da ANP (2004 a 2025),
mantendo as datas como estão (sem conversão), e gera 5 arquivos CSV com separador ';'.
"""

import pandas as pd
import os

# Caminho base dos arquivos
BASE_PATH = r"C:\Users\Emanuel\Documents\InteligenciaMercado\data\transport\anp_diesel_raw"

# Configuração dos arquivos
FILES_INFO = {
    "2004-2012": {
        "file": "semanal-municipios-2004-a-2012.xlsb",
        "sheet": "MUNICÍPIOS - 9.05.04 A 29.12.12",
        "skiprows": 12,
        "engine": "pyxlsb"
    },
    "2013-2017": {
        "file": "semanal-municipios-2013-a-2017.xlsb",
        "sheet": "MUNICÍPIOS -30.12.12 A 28.12.13",
        "skiprows": 14,
        "engine": "pyxlsb"
    },
    "2018-2021": {
        "file": "semanal-municipios-2018-a-2021.xlsb",
        "sheet": "MUNICÍPIOS-31.12.17 A 01.01.22",
        "skiprows": 13,
        "engine": "pyxlsb"
    },
    "2022-2023": {
        "file": "semanal-municipios-2022_a_2023.xlsx",
        "sheet": "MUNICÍPIOS - DESDE 02.01.22",
        "skiprows": 11,
        "engine": None
    },
    "2024-2025": {
        "file": "semanal-municipios-2024-2025.xlsx",
        "sheet": "MUNICÍPIOS - DESDE 31.12.23",
        "skiprows": 11,
        "engine": None
    }
}


def extrair_diesel_sem_conversao(periodo, info):
    caminho = os.path.join(BASE_PATH, info["file"])
    print(f"📥 Extraindo: {info['file']}")

    df = pd.read_excel(
        caminho,
        sheet_name=info["sheet"],
        skiprows=info["skiprows"],
        engine=info["engine"],
        dtype=str  # força leitura como string (inclusive datas)
    )

    # Filtrar apenas Diesel (em qualquer caixa)
    df = df[df["PRODUTO"].str.upper().str.contains("DIESEL", na=False)].copy()

    # Adicionar coluna com origem do arquivo
    df["fonte_arquivo"] = info["file"]

    # Selecionar e ordenar colunas padrão
    colunas = [
        "DATA INICIAL", "DATA FINAL", "REGIÃO", "ESTADO", "MUNICÍPIO",
        "PRODUTO", "PREÇO MÉDIO REVENDA", "fonte_arquivo"
    ]

    # Salva sem transformar datas
    output_csv = os.path.join(BASE_PATH, f"{periodo}.csv")
    df[colunas].to_csv(output_csv, sep=";", index=False, encoding="utf-8-sig")

    print(f"✅ CSV salvo: {output_csv}\n")


def main():
    for periodo, info in FILES_INFO.items():
        extrair_diesel_sem_conversao(periodo, info)


if __name__ == "__main__":
    main()
