"""
📊 Índice de Atividade Econômica (IBC-Br) - dessazonalizado
📅 Periodicidade: Mensal
🔢 Código SGS: 24363
"""

"""
Script para coletar o IBC-Br mensal dessazonalizado (proxy do PIB) via API do Banco Central.
"""

from buildrate.utils.sgs_downloader import baixar_serie_sgs

if __name__ == "__main__":
    baixar_serie_sgs(
        codigo_sgs=24363,  # IBC-Br dessazonalizado (mensal)
        nome_serie="IBC-Br",
        salvar_em="data/macro/ibcbr.csv",
        inicio="01/01/2010"
    )
