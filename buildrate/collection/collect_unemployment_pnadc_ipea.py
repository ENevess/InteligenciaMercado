# buildrate/collection/collect_unemployment_pnadc_ipea.py

"""
Script para coleta da Taxa de Desemprego mensal (PNAD Contínua ajustada) via IPEAData
Ticker: PNADC12_TDESOCM12
Fonte: IPEAData (https://www.ipeadata.gov.br)
Periodicidade: Mensal
Cobertura: Brasil
"""

import pandas as pd
import ipeadatapy

def coletar_taxa_desemprego_pnadc():
    # Coleta dos dados
    df = ipeadatapy.timeseries('PNADC12_TDESOCM12')

    # Filtro a partir de janeiro de 2010
    df = df[df.index >= '2010-01-01']

    # Identifica o nome real da coluna numérica
    nome_coluna_valor = [col for col in df.columns if 'VALUE' in col.upper()][0]

    # Arredonda e renomeia
    df['taxa_desemprego'] = df[nome_coluna_valor].round(1)

    # Mantém apenas coluna final
    df = df[['taxa_desemprego']]
    df.index.name = 'data'

    # Salva CSV
    df.to_csv('data/macro/unemployment_rate_pnadc_ipea.csv')
    print("✅ Dados salvos em: data/macro/unemployment_rate_pnadc_ipea.csv")

if __name__ == "__main__":
    coletar_taxa_desemprego_pnadc()
