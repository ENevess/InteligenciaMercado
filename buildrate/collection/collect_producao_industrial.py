"""
📊 Produção Industrial Mensal
📅 Periodicidade: Mensal
🔢 Código SGS: 21859
"""

"""
Script para coletar a Produção Industrial Mensal via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=21859,  # Produção industrial - índice geral
        nome_serie="Produção Industrial",
        salvar_em="data/macro/producao_industrial.csv",
        inicio="01/01/2010"
    )
