"""
Utilitário para baixar séries temporais do SGS (Banco Central do Brasil)
Divide a consulta em blocos de 1 ano para evitar erro de timeout (504).
"""

import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import time


def baixar_serie_sgs(codigo_sgs: int, nome_serie: str, salvar_em: str, inicio: str = "01/01/2010"):
    """
    Baixa uma série temporal do SGS em blocos anuais e salva como CSV.

    Args:
        codigo_sgs (int): Código da série na API SGS
        nome_serie (str): Nome amigável (para logs)
        salvar_em (str): Caminho para salvar o arquivo CSV
        inicio (str): Data de início da coleta (formato dd/mm/yyyy)
    """
    data_inicio = datetime.strptime(inicio, "%d/%m/%Y")
    data_fim = datetime.now()
    intervalo = timedelta(days=365)

    df_final = pd.DataFrame()

    print(f"[INÍCIO] Série: {nome_serie} (Código SGS: {codigo_sgs})")

    while data_inicio < data_fim:
        data_fim_bloco = min(data_inicio + intervalo, data_fim)

        url = (
            f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_sgs}/dados?"
            f"formato=json&dataInicial={data_inicio.strftime('%d/%m/%Y')}"
            f"&dataFinal={data_fim_bloco.strftime('%d/%m/%Y')}"
        )

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            dados = response.json()

            df = pd.DataFrame(dados)
            df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
            df["valor"] = df["valor"].str.replace(",", ".").astype(float)

            df_final = pd.concat([df_final, df], ignore_index=True)
            print(f"  [OK] {data_inicio.date()} → {data_fim_bloco.date()}")

        except Exception as e:
            print(f"  [ERRO] {data_inicio.date()} → {data_fim_bloco.date()} :: {str(e)}")
            time.sleep(5)  # Espera 5 segundos antes de tentar o próximo bloco

        data_inicio = data_fim_bloco + timedelta(days=1)

    # Cria diretório, ordena e salva CSV
    os.makedirs(os.path.dirname(salvar_em), exist_ok=True)
    df_final.sort_values("data", inplace=True)
    df_final.drop_duplicates("data", inplace=True)
    df_final.to_csv(salvar_em, index=False)

    print(f"[FIM] Dados salvos em: {salvar_em}")
